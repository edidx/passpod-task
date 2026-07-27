import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_INVALID_CODES = {
    "close-before-agree.json": "CLOSE_BEFORE_AGREE",
    "duplicate-message-id.json": "DUPLICATE_MESSAGE_ID",
    "invalid-transition.json": "INVALID_TRANSITION",
    "missing-parent.json": "PARENT_REQUIRED",
    "redefine-message-type.json": "CORE_SEMANTIC_REDEFINITION",
}


def run_cli(*args):
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, "-m", "passpod.cli", *args],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def write_json(directory, name, value):
    path = Path(directory) / name
    path.write_text(json.dumps(value), encoding="utf-8")
    return path


def assert_no_traceback(test_case, result):
    test_case.assertNotIn("Traceback", result.stdout)
    test_case.assertNotIn("Traceback", result.stderr)


class ValidateCommandTests(unittest.TestCase):
    def test_validate_human_success_for_supported_artifacts(self):
        cases = [
            ("message", ROOT / "examples" / "valid" / "minimal-propose.json"),
            ("handshake", ROOT / "examples" / "valid" / "complete-handshake.json"),
            ("profile", ROOT / "examples" / "valid" / "minimal-profile.json"),
        ]

        for artifact_type, path in cases:
            with self.subTest(artifact_type=artifact_type):
                result = run_cli("validate", str(path))

                self.assertEqual(0, result.returncode, result.stderr)
                self.assertEqual(f"VALID {artifact_type}\n", result.stdout)
                self.assertEqual("", result.stderr)

    def test_validate_json_success(self):
        result = run_cli(
            "validate",
            str(ROOT / "examples" / "valid" / "complete-handshake.json"),
            "--json",
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            {
                "valid": True,
                "artifact_type": "handshake",
                "errors": [],
            },
            json.loads(result.stdout),
        )
        self.assertEqual("", result.stderr)

    def test_validate_semantic_failures_preserve_validator_codes(self):
        for path in sorted((ROOT / "examples" / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                result = run_cli("validate", str(path))

                self.assertEqual(1, result.returncode)
                self.assertEqual("", result.stdout)
                self.assertIn("INVALID ", result.stderr)
                self.assertIn(EXPECTED_INVALID_CODES[path.name], result.stderr)
                assert_no_traceback(self, result)

    def test_validate_json_semantic_failure_preserves_validator_errors(self):
        result = run_cli(
            "validate",
            str(ROOT / "examples" / "invalid" / "missing-parent.json"),
            "--json",
        )

        payload = json.loads(result.stderr)
        self.assertEqual(1, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertFalse(payload["valid"])
        self.assertEqual("handshake", payload["artifact_type"])
        self.assertIn("PARENT_REQUIRED", [error["code"] for error in payload["errors"]])
        assert_no_traceback(self, result)

    def test_validate_rejects_empty_handshake(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_json(
                directory,
                "empty-handshake.json",
                {"handshakeIdentity": "hs-empty-001", "messages": []},
            )

            result = run_cli("validate", str(path), "--json")

            payload = json.loads(result.stderr)
            self.assertEqual(1, result.returncode)
            self.assertEqual("", result.stdout)
            self.assertFalse(payload["valid"])
            self.assertEqual("handshake", payload["artifact_type"])
            self.assertIn("SCHEMA_INVALID", [error["code"] for error in payload["errors"]])
            assert_no_traceback(self, result)

    def test_validate_rejects_missing_messages(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_json(
                directory,
                "missing-messages.json",
                {"handshakeIdentity": "hs-missing-001"},
            )

            result = run_cli("validate", str(path), "--json")

            payload = json.loads(result.stderr)
            self.assertEqual(2, result.returncode)
            self.assertEqual("", result.stdout)
            self.assertFalse(payload["valid"])
            self.assertIsNone(payload["artifact_type"])
            self.assertEqual("ARTIFACT_TYPE_UNKNOWN", payload["errors"][0]["code"])
            assert_no_traceback(self, result)


class InputFailureTests(unittest.TestCase):
    def test_detection_and_input_failures_are_exit_code_2(self):
        with tempfile.TemporaryDirectory() as directory:
            malformed = Path(directory) / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            non_object = Path(directory) / "non-object.json"
            non_object.write_text("[]", encoding="utf-8")
            unknown = write_json(directory, "unknown.json", {"hello": "world"})
            ambiguous = write_json(
                directory,
                "ambiguous.json",
                {
                    "messageIdentity": "msg-ambiguous-001",
                    "messageType": "PROPOSE",
                    "profileIdentity": "profile-ambiguous-001",
                    "profileVersion": "0.1",
                    "lifecycle": "draft",
                },
            )

            cases = [
                ("FILE_NOT_FOUND", Path(directory) / "missing.json"),
                ("JSON_INVALID", malformed),
                ("ROOT_NOT_OBJECT", non_object),
                ("ARTIFACT_TYPE_UNKNOWN", unknown),
                ("ARTIFACT_TYPE_AMBIGUOUS", ambiguous),
            ]

            for code, path in cases:
                with self.subTest(code=code):
                    result = run_cli("validate", str(path))

                    self.assertEqual(2, result.returncode)
                    self.assertEqual("", result.stdout)
                    self.assertIn(code, result.stderr)
                    assert_no_traceback(self, result)

    def test_json_input_failure_uses_cli_error_code(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_json(directory, "unknown.json", {"hello": "world"})

            result = run_cli("validate", str(path), "--json")

            payload = json.loads(result.stderr)
            self.assertEqual(2, result.returncode)
            self.assertEqual("", result.stdout)
            self.assertEqual("ARTIFACT_TYPE_UNKNOWN", payload["errors"][0]["code"])
            self.assertIsNone(payload["artifact_type"])
            assert_no_traceback(self, result)


class InspectCommandTests(unittest.TestCase):
    def test_inspect_message_human_summary(self):
        result = run_cli("inspect", str(ROOT / "examples" / "valid" / "minimal-propose.json"))

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("", result.stderr)
        self.assertIn("artifact_type: message\n", result.stdout)
        self.assertIn("message_identity: msg-propose-001\n", result.stdout)
        self.assertIn("handshake_identity: hs-minimal-propose-001\n", result.stdout)
        self.assertIn("message_type: PROPOSE\n", result.stdout)
        self.assertIn("parent_reference: null\n", result.stdout)
        self.assertIn("sender_present: true\n", result.stdout)
        self.assertIn("recipient_present: false\n", result.stdout)

    def test_inspect_handshake_json_summary(self):
        result = run_cli(
            "inspect",
            str(ROOT / "examples" / "valid" / "complete-handshake.json"),
            "--json",
        )

        payload = json.loads(result.stdout)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("", result.stderr)
        self.assertEqual("handshake", payload["artifact_type"])
        self.assertEqual("closed", payload["state"])
        self.assertTrue(payload["closed"])
        self.assertEqual(4, payload["message_count"])
        self.assertEqual(
            [
                {"message_identity": "msg-propose-001", "message_type": "PROPOSE"},
                {"message_identity": "msg-challenge-001", "message_type": "CHALLENGE"},
                {"message_identity": "msg-agree-001", "message_type": "AGREE"},
                {"message_identity": "msg-close-001", "message_type": "CLOSE"},
            ],
            payload["messages"],
        )

    def test_inspect_profile_human_summary(self):
        result = run_cli("inspect", str(ROOT / "examples" / "valid" / "minimal-profile.json"))

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("", result.stderr)
        self.assertIn("artifact_type: profile\n", result.stdout)
        self.assertIn("profile_identity: profile-minimal-001\n", result.stdout)
        self.assertIn("profile_version: 0.1\n", result.stdout)
        self.assertIn("lifecycle: draft\n", result.stdout)
        self.assertNotIn("Minimal Profile Model Example", result.stdout)

    def test_inspect_rejects_invalid_artifact(self):
        result = run_cli("inspect", str(ROOT / "examples" / "invalid" / "invalid-transition.json"))

        self.assertEqual(1, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertIn("INVALID handshake", result.stderr)
        self.assertIn("INVALID_TRANSITION", result.stderr)
        assert_no_traceback(self, result)


class InspectPrivacyTests(unittest.TestCase):
    def test_inspect_does_not_expose_sensitive_payloads(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_json(
                directory,
                "private-message.json",
                {
                    "messageIdentity": "msg-private-001",
                    "handshakeIdentity": "hs-private-001",
                    "messageType": "PROPOSE",
                    "sender": {"id": "participant-alpha", "secret": "sender-secret"},
                    "recipient": {"id": "participant-beta", "secret": "recipient-secret"},
                    "evidenceReferences": [{"secretEvidence": "evidence-secret"}],
                    "extensions": {"privateExtension": "extension-secret"},
                },
            )

            human = run_cli("inspect", str(path))
            machine = run_cli("inspect", str(path), "--json")
            combined = human.stdout + human.stderr + machine.stdout + machine.stderr

            self.assertEqual(0, human.returncode, human.stderr)
            self.assertEqual(0, machine.returncode, machine.stderr)
            self.assertIn("sender_present: true", human.stdout)
            self.assertIn("recipient_present: true", human.stdout)
            self.assertNotIn("sender-secret", combined)
            self.assertNotIn("recipient-secret", combined)
            self.assertNotIn("evidence-secret", combined)
            self.assertNotIn("extension-secret", combined)


if __name__ == "__main__":
    unittest.main()
