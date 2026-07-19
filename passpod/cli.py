import argparse
import json
import sys

from . import Handshake, Message, PasspodValidationError, Profile


EXIT_SUCCESS = 0
EXIT_INVALID = 1
EXIT_INPUT_ERROR = 2

FILE_NOT_FOUND = "FILE_NOT_FOUND"
FILE_READ_ERROR = "FILE_READ_ERROR"
JSON_INVALID = "JSON_INVALID"
ROOT_NOT_OBJECT = "ROOT_NOT_OBJECT"
ARTIFACT_TYPE_UNKNOWN = "ARTIFACT_TYPE_UNKNOWN"
ARTIFACT_TYPE_AMBIGUOUS = "ARTIFACT_TYPE_AMBIGUOUS"


class CliError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)


def main(argv=None):
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        mapping = _load_mapping(args.path)
        artifact_type = detect_artifact_type(mapping)
    except CliError as error:
        return _emit_cli_error(error, args.json)

    if args.command == "validate":
        return _validate(artifact_type, mapping, args.json)
    if args.command == "inspect":
        return _inspect(artifact_type, mapping, args.json)

    parser.error(f"unsupported command: {args.command}")
    return EXIT_INPUT_ERROR


def _build_parser():
    parser = argparse.ArgumentParser(prog="python3 -m passpod.cli")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("validate", "inspect"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("path")
        subparser.add_argument("--json", action="store_true", dest="json")

    return parser


def _load_mapping(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as error:
        raise CliError(FILE_NOT_FOUND, "File was not found.") from error
    except json.JSONDecodeError as error:
        message = f"JSON is malformed at line {error.lineno}, column {error.colno}."
        raise CliError(JSON_INVALID, message) from error
    except OSError as error:
        raise CliError(FILE_READ_ERROR, "File could not be read.") from error

    if not isinstance(value, dict):
        raise CliError(ROOT_NOT_OBJECT, "JSON root must be an object.")

    return value


def detect_artifact_type(mapping):
    matches = []

    if {"messageIdentity", "messageType"}.issubset(mapping):
        matches.append("message")
    if {"handshakeIdentity", "messages"}.issubset(mapping):
        matches.append("handshake")
    if {"profileIdentity", "profileVersion", "lifecycle"}.issubset(mapping):
        matches.append("profile")

    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise CliError(ARTIFACT_TYPE_UNKNOWN, "Artifact type could not be determined.")

    raise CliError(
        ARTIFACT_TYPE_AMBIGUOUS,
        "Artifact matches multiple top-level artifact shapes.",
    )


def _validate(artifact_type, mapping, as_json):
    try:
        _construct_object(artifact_type, mapping)
    except PasspodValidationError as error:
        return _emit_validation_failure(artifact_type, error.errors, as_json)

    payload = {
        "valid": True,
        "artifact_type": artifact_type,
        "errors": [],
    }
    if as_json:
        _write_json(sys.stdout, payload)
    else:
        print(f"VALID {artifact_type}")
    return EXIT_SUCCESS


def _inspect(artifact_type, mapping, as_json):
    try:
        value = _construct_object(artifact_type, mapping)
    except PasspodValidationError as error:
        return _emit_validation_failure(artifact_type, error.errors, as_json)

    summary = _summary(artifact_type, value)
    if as_json:
        _write_json(sys.stdout, summary)
    else:
        _write_human_summary(summary)
    return EXIT_SUCCESS


def _construct_object(artifact_type, mapping):
    if artifact_type == "message":
        return Message.from_mapping(mapping)
    if artifact_type == "handshake":
        return Handshake.from_mapping(mapping)
    if artifact_type == "profile":
        return Profile.from_mapping(mapping)
    raise CliError(ARTIFACT_TYPE_UNKNOWN, "Artifact type could not be determined.")


def _summary(artifact_type, value):
    if artifact_type == "message":
        return {
            "artifact_type": "message",
            "message_identity": value.message_identity,
            "handshake_identity": value.handshake_identity,
            "message_type": value.message_type,
            "parent_reference": value.parent_reference,
            "sender_present": value.sender is not None,
            "recipient_present": value.recipient is not None,
        }

    if artifact_type == "handshake":
        return {
            "artifact_type": "handshake",
            "handshake_identity": value.handshake_identity,
            "state": value.lifecycle,
            "closed": value.is_closed,
            "message_count": value.message_count,
            "messages": [
                {
                    "message_identity": message.message_identity,
                    "message_type": message.message_type,
                }
                for message in value.history
            ],
        }

    if artifact_type == "profile":
        return {
            "artifact_type": "profile",
            "profile_identity": value.profile_identity,
            "profile_version": value.profile_version,
            "lifecycle": value.lifecycle,
        }

    raise CliError(ARTIFACT_TYPE_UNKNOWN, "Artifact type could not be determined.")


def _emit_validation_failure(artifact_type, errors, as_json):
    payload = {
        "valid": False,
        "artifact_type": artifact_type,
        "errors": list(errors),
    }
    if as_json:
        _write_json(sys.stderr, payload)
    else:
        print(f"INVALID {artifact_type}", file=sys.stderr)
        for error in errors:
            code = error.get("code", "UNKNOWN")
            path = error.get("path", "$")
            message = error.get("message", "")
            print(f"{code} {path}: {message}", file=sys.stderr)
    return EXIT_INVALID


def _emit_cli_error(error, as_json):
    payload = {
        "valid": False,
        "artifact_type": None,
        "errors": [
            {
                "code": error.code,
                "path": "$",
                "message": error.message,
            }
        ],
    }
    if as_json:
        _write_json(sys.stderr, payload)
    else:
        print(f"ERROR {error.code}: {error.message}", file=sys.stderr)
    return EXIT_INPUT_ERROR


def _write_human_summary(summary):
    for key, value in summary.items():
        if key == "messages":
            print("messages:")
            for message in value:
                print(f"- {_format_value(message['message_identity'])} {_format_value(message['message_type'])}")
        else:
            print(f"{key}: {_format_value(value)}")


def _write_json(stream, payload):
    stream.write(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    stream.write("\n")


def _format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (dict, list)):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    return str(value)


if __name__ == "__main__":
    raise SystemExit(main())
