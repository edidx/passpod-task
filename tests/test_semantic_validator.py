import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "validator" / "semantic_validator.py"

spec = importlib.util.spec_from_file_location("semantic_validator", MODULE_PATH)
semantic_validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(semantic_validator)


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate_fixture(path):
    data = load_json(path)
    if "profileIdentity" in data:
        return semantic_validator.validateProfile(data)
    if "messages" in data:
        return semantic_validator.validateHandshake(data)
    return semantic_validator.validateMessage(data)


def error_codes(result):
    return [error["code"] for error in result["errors"]]


class FixtureValidationTests(unittest.TestCase):
    def test_valid_fixtures_pass(self):
        for path in sorted((ROOT / "examples" / "valid").glob("*.json")):
            with self.subTest(path=path.name):
                result = validate_fixture(path.relative_to(ROOT))
                self.assertTrue(result["valid"], result["errors"])
                self.assertEqual([], result["errors"])

    def test_invalid_fixtures_fail_with_expected_codes(self):
        expected = {
            "missing-parent.json": semantic_validator.PARENT_REQUIRED,
            "invalid-transition.json": semantic_validator.INVALID_TRANSITION,
            "close-before-agree.json": semantic_validator.CLOSE_BEFORE_AGREE,
            "duplicate-message-id.json": semantic_validator.DUPLICATE_MESSAGE_ID,
            "redefine-message-type.json": semantic_validator.CORE_SEMANTIC_REDEFINITION,
        }

        for path in sorted((ROOT / "examples" / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                result = validate_fixture(path.relative_to(ROOT))
                self.assertFalse(result["valid"])
                self.assertIn(expected[path.name], error_codes(result))


class DirectSemanticRuleTests(unittest.TestCase):
    def handshake(self, messages, **extra):
        data = {
            "handshakeIdentity": "hs-direct-001",
            "lifecycle": extra.pop("lifecycle", "challenged"),
            "messages": messages,
        }
        data.update(extra)
        return data

    def message(self, identity, message_type, parent=None, handshake_identity="hs-direct-001"):
        data = {
            "messageIdentity": identity,
            "handshakeIdentity": handshake_identity,
            "messageType": message_type,
            "sender": "participant-alpha",
        }
        if parent is not None:
            data["parentReference"] = parent
        return data

    def assert_has_code(self, result, code):
        self.assertFalse(result["valid"])
        self.assertIn(code, error_codes(result))

    def test_empty_or_missing_messages(self):
        for handshake in (
            {"handshakeIdentity": "hs-direct-001", "messages": []},
            {"handshakeIdentity": "hs-direct-001"},
        ):
            with self.subTest(handshake=handshake):
                result = semantic_validator.validateHandshake(handshake)
                self.assert_has_code(result, semantic_validator.SCHEMA_INVALID)

    def test_duplicate_message_identity(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-1", "CHALLENGE", parent="msg-1"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.DUPLICATE_MESSAGE_ID)

    def test_mismatched_handshake_identity(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="msg-1", handshake_identity="other"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.HANDSHAKE_ID_MISMATCH)

    def test_missing_parent(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.PARENT_REQUIRED)

    def test_nonexistent_parent(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="missing"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.PARENT_NOT_FOUND)

    def test_self_parent_reference(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="msg-2"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.PARENT_SELF_REFERENCE)

    def test_forward_parent_reference(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="msg-3"),
                    self.message("msg-3", "CHALLENGE", parent="msg-2"),
                ]
            )
        )
        self.assert_has_code(result, semantic_validator.PARENT_NOT_EARLIER)

    def test_first_message_not_propose(self):
        result = semantic_validator.validateHandshake(
            self.handshake([self.message("msg-1", "CHALLENGE")])
        )
        self.assert_has_code(result, semantic_validator.INITIAL_MESSAGE_NOT_PROPOSE)

    def test_invalid_lifecycle_transition(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "AGREE", parent="msg-1"),
                ],
                lifecycle="agreed",
            )
        )
        self.assert_has_code(result, semantic_validator.INVALID_TRANSITION)

    def test_message_after_close(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="msg-1"),
                    self.message("msg-3", "AGREE", parent="msg-2"),
                    self.message("msg-4", "CLOSE", parent="msg-3"),
                    self.message("msg-5", "CHALLENGE", parent="msg-4"),
                ],
                lifecycle="closed",
                terminalClosure={
                    "isClosed": True,
                    "outcome": "completed",
                    "closeMessageReference": "msg-4",
                },
            )
        )
        self.assert_has_code(result, semantic_validator.MESSAGE_AFTER_CLOSE)

    def test_close_before_agree(self):
        result = semantic_validator.validateHandshake(
            self.handshake(
                [
                    self.message("msg-1", "PROPOSE"),
                    self.message("msg-2", "CHALLENGE", parent="msg-1"),
                    self.message("msg-3", "CLOSE", parent="msg-2"),
                ],
                lifecycle="closed",
                terminalClosure={
                    "isClosed": True,
                    "outcome": "completed",
                    "closeMessageReference": "msg-3",
                },
            )
        )
        self.assert_has_code(result, semantic_validator.CLOSE_BEFORE_AGREE)

    def test_profile_attempt_to_redefine_canonical_message_type(self):
        profile = {
            "profileIdentity": "profile-direct-invalid-001",
            "profileVersion": "0.1",
            "lifecycle": "draft",
            "mayDefine": {
                "terminology": {
                    "PROPOSE": "Invalid attempt to redefine PROPOSE."
                }
            },
        }
        result = semantic_validator.validateProfile(profile)
        self.assert_has_code(result, semantic_validator.CORE_SEMANTIC_REDEFINITION)


if __name__ == "__main__":
    unittest.main()
