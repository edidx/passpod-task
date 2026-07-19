#!/usr/bin/env python3
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

SCHEMA_INVALID = "SCHEMA_INVALID"
DUPLICATE_MESSAGE_ID = "DUPLICATE_MESSAGE_ID"
HANDSHAKE_ID_MISMATCH = "HANDSHAKE_ID_MISMATCH"
INITIAL_MESSAGE_NOT_PROPOSE = "INITIAL_MESSAGE_NOT_PROPOSE"
PARENT_REQUIRED = "PARENT_REQUIRED"
PARENT_NOT_FOUND = "PARENT_NOT_FOUND"
PARENT_SELF_REFERENCE = "PARENT_SELF_REFERENCE"
PARENT_NOT_EARLIER = "PARENT_NOT_EARLIER"
INVALID_TRANSITION = "INVALID_TRANSITION"
MESSAGE_AFTER_CLOSE = "MESSAGE_AFTER_CLOSE"
CLOSE_BEFORE_AGREE = "CLOSE_BEFORE_AGREE"
CORE_SEMANTIC_REDEFINITION = "CORE_SEMANTIC_REDEFINITION"

CORE_MESSAGE_TYPES = ("PROPOSE", "CHALLENGE", "AGREE", "CLOSE")
FORBIDDEN_PROFILE_REDEFINITIONS = (
    "PROPOSE",
    "CHALLENGE",
    "AGREE",
    "CLOSE",
    "append-only history",
    "immutable accepted messages",
    "Standard semantics",
    "Protocol semantics",
)


def validateMessage(message):
    errors = _schema_errors("message", message)
    errors.extend(_core_redefinition_errors(message))
    return _result(errors)


def validateHandshake(handshake):
    errors = _schema_errors("handshake", handshake)

    if not isinstance(handshake, dict):
        return _result(errors)

    messages = handshake.get("messages")
    if not isinstance(messages, list):
        return _result(errors)

    for index, message in enumerate(messages):
        if isinstance(message, dict):
            errors.extend(_message_schema_errors_in_handshake(index, message))

    handshake_identity = handshake.get("handshakeIdentity")
    message_positions = {}
    message_ids = []

    for index, message in enumerate(messages):
        if not isinstance(message, dict):
            continue

        message_identity = message.get("messageIdentity")
        message_ids.append(message_identity)
        identity_key = _identity_key(message_identity)

        if identity_key in message_positions:
            errors.append(
                _error(
                    DUPLICATE_MESSAGE_ID,
                    f"messages[{index}].messageIdentity",
                    "Message identity must be unique within one handshake.",
                    handshake_identity=handshake_identity,
                    message_identity=message_identity,
                )
            )
        else:
            message_positions[identity_key] = index

        if not _same_identity(message.get("handshakeIdentity"), handshake_identity):
            errors.append(
                _error(
                    HANDSHAKE_ID_MISMATCH,
                    f"messages[{index}].handshakeIdentity",
                    "Message handshake identity must match the enclosing handshake identity.",
                    handshake_identity=handshake_identity,
                    message_identity=message_identity,
                )
            )

        errors.extend(_core_redefinition_errors(message, path_prefix=f"messages[{index}]"))

    if messages:
        first = messages[0]
        first_type = first.get("messageType") if isinstance(first, dict) else None
        first_identity = first.get("messageIdentity") if isinstance(first, dict) else None

        if first_type != "PROPOSE":
            errors.append(
                _error(
                    INITIAL_MESSAGE_NOT_PROPOSE,
                    "messages[0].messageType",
                    "The first accepted message must be PROPOSE.",
                    handshake_identity=handshake_identity,
                    message_identity=first_identity,
                )
            )

    parent_map = _parent_map(handshake)
    seen_agree = False
    closed = False
    previous_type = None

    for index, message in enumerate(messages):
        if not isinstance(message, dict):
            continue

        message_type = message.get("messageType")
        message_identity = message.get("messageIdentity")

        if closed:
            errors.append(
                _error(
                    MESSAGE_AFTER_CLOSE,
                    f"messages[{index}].messageType",
                    "No message may follow CLOSE.",
                    handshake_identity=handshake_identity,
                    message_identity=message_identity,
                )
            )
            continue

        if index > 0:
            parent_refs = _message_parent_refs(message, parent_map)
            if not parent_refs:
                errors.append(
                    _error(
                        PARENT_REQUIRED,
                        f"messages[{index}].parentReference",
                        "Every non-initial message must have an applicable parent reference.",
                        handshake_identity=handshake_identity,
                        message_identity=message_identity,
                    )
                )

            for parent_ref in parent_refs:
                parent_key = _identity_key(parent_ref)
                if _same_identity(parent_ref, message_identity):
                    errors.append(
                        _error(
                            PARENT_SELF_REFERENCE,
                            f"messages[{index}].parentReference",
                            "A message must not reference itself as parent.",
                            handshake_identity=handshake_identity,
                            message_identity=message_identity,
                        )
                    )
                    continue

                parent_index = message_positions.get(parent_key)
                if parent_index is None:
                    errors.append(
                        _error(
                            PARENT_NOT_FOUND,
                            f"messages[{index}].parentReference",
                            "A parent reference must identify an accepted message in the same handshake.",
                            handshake_identity=handshake_identity,
                            message_identity=message_identity,
                        )
                    )
                    continue

                if parent_index >= index:
                    errors.append(
                        _error(
                            PARENT_NOT_EARLIER,
                            f"messages[{index}].parentReference",
                            "A parent reference must identify an earlier accepted message.",
                            handshake_identity=handshake_identity,
                            message_identity=message_identity,
                        )
                    )

        transition_error = _transition_error(previous_type, message_type, index, seen_agree, handshake)
        if transition_error:
            code, message_text = transition_error
            errors.append(
                _error(
                    code,
                    f"messages[{index}].messageType",
                    message_text,
                    handshake_identity=handshake_identity,
                    message_identity=message_identity,
                )
            )

        if message_type == "AGREE":
            seen_agree = True

        if message_type == "CLOSE":
            closed = True

        previous_type = message_type

    return _result(errors)


def validateProfile(profile):
    errors = _schema_errors("profile", profile)
    errors.extend(_profile_redefinition_errors(profile))
    return _result(errors)


def _result(errors):
    return {
        "valid": not errors,
        "errors": errors,
    }


def _load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_for(kind):
    if kind == "message":
        return _load_json(SCHEMAS / "message.schema.json")
    if kind == "profile":
        return _load_json(SCHEMAS / "profile.schema.json")
    if kind == "handshake":
        schema = _load_json(SCHEMAS / "handshake.schema.json")
        schema = copy.deepcopy(schema)
        schema["properties"]["messages"]["items"] = {"type": "object"}
        return schema
    raise ValueError(f"Unknown schema kind: {kind}")


def _schema_errors(kind, instance):
    schema = _schema_for(kind)
    validator = Draft202012Validator(schema)
    errors = []

    for schema_error in sorted(validator.iter_errors(instance), key=_schema_error_sort_key):
        errors.append(
            _error(
                SCHEMA_INVALID,
                _schema_path(schema_error),
                f"Schema validation failed: {schema_error.message}",
                handshake_identity=_context_value(instance, "handshakeIdentity"),
                message_identity=_context_value(instance, "messageIdentity"),
            )
        )

    return errors


def _message_schema_errors_in_handshake(index, message):
    errors = _schema_errors("message", message)
    for error in errors:
        error["path"] = _prefix_path(f"$.messages[{index}]", error["path"])
    return errors


def _schema_error_sort_key(schema_error):
    return (list(schema_error.path), schema_error.message)


def _schema_path(schema_error):
    parts = list(schema_error.path)
    if not parts:
        return "$"

    path = "$"
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"
    return path


def _prefix_path(prefix, path):
    if path == "$":
        return prefix
    if path.startswith("$."):
        return prefix + path[1:]
    if path.startswith("$["):
        return prefix + path[1:]
    return f"{prefix}.{path}"


def _context_value(value, key):
    if isinstance(value, dict):
        return value.get(key)
    return None


def _error(code, path, message, handshake_identity=None, message_identity=None):
    error = {
        "code": code,
        "path": path,
        "message": message,
    }

    if message_identity is not None:
        error["messageIdentity"] = message_identity

    if handshake_identity is not None:
        error["handshakeIdentity"] = handshake_identity

    return error


def _identity_key(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _same_identity(left, right):
    return _identity_key(left) == _identity_key(right)


def _parent_map(handshake):
    parent_map = {}
    relationships = handshake.get("parentRelationships", [])
    if not isinstance(relationships, list):
        return parent_map

    for relationship in relationships:
        if not isinstance(relationship, dict):
            continue
        message_ref = relationship.get("messageReference")
        parent_ref = relationship.get("parentReference")
        if message_ref is None or parent_ref is None:
            continue
        parent_map.setdefault(_identity_key(message_ref), []).append(parent_ref)

    return parent_map


def _message_parent_refs(message, parent_map):
    parent_refs = []
    if "parentReference" in message:
        parent_refs.append(message.get("parentReference"))

    message_identity = message.get("messageIdentity")
    parent_refs.extend(parent_map.get(_identity_key(message_identity), []))

    unique_refs = []
    seen = set()
    for parent_ref in parent_refs:
        key = _identity_key(parent_ref)
        if key in seen:
            continue
        seen.add(key)
        unique_refs.append(parent_ref)

    return unique_refs


def _transition_error(previous_type, message_type, index, seen_agree, handshake):
    if message_type not in CORE_MESSAGE_TYPES:
        return None

    if index == 0:
        return None

    if message_type == "PROPOSE":
        if previous_type == "CHALLENGE":
            return None
        return (
            INVALID_TRANSITION,
            "A revised PROPOSE is only valid after CHALLENGE in this bounded validator.",
        )

    if message_type == "CHALLENGE":
        if previous_type in ("PROPOSE", "CHALLENGE"):
            return None
        return (
            INVALID_TRANSITION,
            "CHALLENGE must follow proposal or challenge context.",
        )

    if message_type == "AGREE":
        if previous_type == "CHALLENGE":
            return None
        return (
            INVALID_TRANSITION,
            "AGREE must follow resolved negotiation context.",
        )

    if message_type == "CLOSE":
        outcome = _terminal_outcome(handshake)
        if outcome == "completed" and not seen_agree:
            return (
                CLOSE_BEFORE_AGREE,
                "A completed CLOSE must not appear before AGREE.",
            )
        if outcome == "completed" and previous_type != "AGREE":
            return (
                INVALID_TRANSITION,
                "A completed CLOSE must follow AGREE.",
            )
        return None

    return None


def _terminal_outcome(handshake):
    terminal = handshake.get("terminalClosure")
    if isinstance(terminal, dict):
        return terminal.get("outcome")
    return None


def _core_redefinition_errors(value, path_prefix="$"):
    errors = []
    _walk_for_redefinitions(value, path_prefix, errors, profile_mode=False)
    return errors


def _profile_redefinition_errors(profile):
    errors = []
    _walk_for_redefinitions(profile, "$", errors, profile_mode=True)
    return errors


def _walk_for_redefinitions(value, path, errors, profile_mode):
    if isinstance(value, dict):
        if "messageTypeRedefinitions" in value:
            errors.append(
                _error(
                    CORE_SEMANTIC_REDEFINITION,
                    _join_path(path, "messageTypeRedefinitions"),
                    "Extensions may not masquerade as replacement canonical message types.",
                    handshake_identity=value.get("handshakeIdentity"),
                    message_identity=value.get("messageIdentity"),
                )
            )

        if profile_mode and path.endswith(".terminology"):
            for core_type in CORE_MESSAGE_TYPES:
                if core_type in value:
                    errors.append(
                        _error(
                            CORE_SEMANTIC_REDEFINITION,
                            _join_path(path, core_type),
                            "Profiles must not redefine canonical message types.",
                        )
                    )

        for key in FORBIDDEN_PROFILE_REDEFINITIONS:
            if key in value and key != "PROPOSE" and not path.endswith(".terminology"):
                # Canonical terms can appear as data elsewhere; only explicit
                # redefinition containers are rejected by this bounded pass.
                continue

        for child_key, child_value in value.items():
            _walk_for_redefinitions(child_value, _join_path(path, child_key), errors, profile_mode)
        return

    if isinstance(value, list):
        for index, child_value in enumerate(value):
            _walk_for_redefinitions(child_value, f"{path}[{index}]", errors, profile_mode)


def _join_path(path, part):
    if path == "$":
        return f"$.{part}"
    return f"{path}.{part}"
