import json
import unittest
from pathlib import Path

from passpod import Handshake, Message, PasspodValidationError, Profile
from validator.semantic_validator import validateHandshake, validateMessage, validateProfile


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_INVALID_CODES = {
    "close-before-agree.json": "CLOSE_BEFORE_AGREE",
    "duplicate-message-id.json": "DUPLICATE_MESSAGE_ID",
    "invalid-transition.json": "INVALID_TRANSITION",
    "missing-parent.json": "PARENT_REQUIRED",
    "redefine-message-type.json": "CORE_SEMANTIC_REDEFINITION",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sdk_from_mapping(mapping):
    if "profileIdentity" in mapping:
        return Profile.from_mapping(mapping)
    if "messages" in mapping:
        return Handshake.from_mapping(mapping)
    return Message.from_mapping(mapping)


def validate_mapping(mapping):
    if "profileIdentity" in mapping:
        return validateProfile(mapping)
    if "messages" in mapping:
        return validateHandshake(mapping)
    return validateMessage(mapping)


def error_codes(error):
    return [entry["code"] for entry in error.errors]


class FixtureRoundTripTests(unittest.TestCase):
    def test_all_valid_fixtures_round_trip_and_validate(self):
        for path in sorted((ROOT / "examples" / "valid").glob("*.json")):
            with self.subTest(path=path.name):
                original = load_json(path)
                sdk_object = sdk_from_mapping(original)
                round_tripped = sdk_object.to_mapping()

                self.assertEqual(original, round_tripped)
                self.assertIsNot(original, round_tripped)

                result = validate_mapping(round_tripped)
                self.assertTrue(result["valid"], result["errors"])

    def test_all_invalid_fixtures_fail_with_intended_error_codes(self):
        for path in sorted((ROOT / "examples" / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                original = load_json(path)

                with self.assertRaises(PasspodValidationError) as raised:
                    sdk_from_mapping(original)

                self.assertIn(EXPECTED_INVALID_CODES[path.name], error_codes(raised.exception))


class ErgonomicsTests(unittest.TestCase):
    def test_reprs_are_readable_and_bounded(self):
        message = Message.from_mapping(
            {
                "messageIdentity": "msg-repr-001",
                "handshakeIdentity": "hs-repr-001",
                "messageType": "PROPOSE",
                "sender": "participant-alpha",
                "evidenceReferences": ["sensitive-evidence-reference"],
                "extensions": {"largePayload": {"nested": "payload"}},
            }
        )
        handshake = Handshake.from_mapping(load_json(ROOT / "examples" / "valid" / "complete-handshake.json"))
        profile = Profile.from_mapping(load_json(ROOT / "examples" / "valid" / "minimal-profile.json"))

        self.assertEqual(
            "Message(message_identity='msg-repr-001', message_type='PROPOSE', handshake_identity='hs-repr-001')",
            repr(message),
        )
        self.assertIn("Handshake(handshake_identity='hs-complete-001'", repr(handshake))
        self.assertIn("state='closed'", repr(handshake))
        self.assertIn("message_count=4", repr(handshake))
        self.assertEqual(
            "Profile(profile_identity='profile-minimal-001', profile_version='0.1', lifecycle='draft')",
            repr(profile),
        )
        self.assertNotIn("sensitive-evidence-reference", repr(message))
        self.assertNotIn("largePayload", repr(message))

    def test_handshake_read_only_conveniences(self):
        handshake = Handshake.from_mapping(load_json(ROOT / "examples" / "valid" / "complete-handshake.json"))
        last = handshake.last_message

        self.assertEqual(4, handshake.message_count)
        self.assertIs(last, handshake.get_message("msg-close-001"))
        self.assertEqual("CLOSE", last.message_type)
        self.assertIsNone(handshake.get_message("missing"))

    def test_equivalent_value_objects_compare_equal(self):
        message_mapping = load_json(ROOT / "examples" / "valid" / "minimal-propose.json")
        handshake_mapping = load_json(ROOT / "examples" / "valid" / "complete-handshake.json")
        profile_mapping = load_json(ROOT / "examples" / "valid" / "minimal-profile.json")

        self.assertEqual(Message.from_mapping(message_mapping), Message.from_mapping(message_mapping))
        self.assertEqual(Handshake.from_mapping(handshake_mapping), Handshake.from_mapping(handshake_mapping))
        self.assertEqual(Profile.from_mapping(profile_mapping), Profile.from_mapping(profile_mapping))


class DefensiveCopyTests(unittest.TestCase):
    def test_original_mapping_mutation_does_not_affect_sdk_object(self):
        mapping = {
            "messageIdentity": "msg-copy-001",
            "handshakeIdentity": "hs-copy-001",
            "messageType": "PROPOSE",
            "sender": {"id": "participant-alpha"},
            "extensions": {"nested": {"value": "accepted"}},
        }
        message = Message.from_mapping(mapping)

        mapping["sender"]["id"] = "changed"
        mapping["extensions"]["nested"]["value"] = "changed"

        self.assertEqual({"id": "participant-alpha"}, message.sender)
        self.assertEqual("accepted", message.to_mapping()["extensions"]["nested"]["value"])

    def test_to_mapping_mutation_does_not_affect_sdk_object(self):
        message = Message.from_mapping(
            {
                "messageIdentity": "msg-copy-002",
                "handshakeIdentity": "hs-copy-002",
                "messageType": "PROPOSE",
                "sender": "participant-alpha",
                "evidenceReferences": [{"id": "evidence-001"}],
                "extensions": {"nested": {"value": "accepted"}},
            }
        )

        exported = message.to_mapping()
        exported["evidenceReferences"][0]["id"] = "changed"
        exported["extensions"]["nested"]["value"] = "changed"

        fresh = message.to_mapping()
        self.assertEqual("evidence-001", fresh["evidenceReferences"][0]["id"])
        self.assertEqual("accepted", fresh["extensions"]["nested"]["value"])

    def test_handshake_history_cannot_be_changed_through_returned_collections(self):
        handshake = Handshake.from_mapping(load_json(ROOT / "examples" / "valid" / "complete-handshake.json"))
        history = handshake.history

        with self.assertRaises(AttributeError):
            history.append(Message.from_mapping(load_json(ROOT / "examples" / "valid" / "minimal-propose.json")))

        exported = handshake.to_mapping()
        exported["messages"].reverse()

        self.assertEqual("msg-propose-001", handshake.history[0].message_identity)
        self.assertEqual("msg-close-001", handshake.last_message.message_identity)

    def test_prior_handshake_remains_unchanged_after_append(self):
        initial = Message.from_mapping(load_json(ROOT / "examples" / "valid" / "minimal-propose.json"))
        proposed = Handshake("hs-minimal-propose-001", messages=[initial]).append(
            Message.from_mapping(
                {
                    "messageIdentity": "msg-challenge-001",
                    "handshakeIdentity": "hs-minimal-propose-001",
                    "parentReference": "msg-propose-001",
                    "messageType": "CHALLENGE",
                    "sender": "participant-beta",
                }
            )
        )
        agreed = proposed.append(
            Message.from_mapping(
                {
                    "messageIdentity": "msg-agree-001",
                    "handshakeIdentity": "hs-minimal-propose-001",
                    "parentReference": "msg-challenge-001",
                    "messageType": "AGREE",
                    "sender": "participant-alpha",
                }
            )
        )

        self.assertEqual(2, proposed.message_count)
        self.assertEqual(3, agreed.message_count)
        self.assertEqual("CHALLENGE", proposed.last_message.message_type)
        self.assertEqual("AGREE", agreed.last_message.message_type)


class ExceptionErgonomicsTests(unittest.TestCase):
    def test_error_access_is_defensive_and_string_is_readable(self):
        with self.assertRaises(PasspodValidationError) as raised:
            Message.from_mapping(
                {
                    "messageIdentity": "msg-error-001",
                    "handshakeIdentity": "hs-error-001",
                    "messageType": "UNKNOWN",
                    "sender": "participant-alpha",
                }
            )

        error = raised.exception
        errors = error.errors
        errors[0]["code"] = "MUTATED"

        self.assertEqual("validateMessage", error.operation)
        self.assertIn("validateMessage failed validation: SCHEMA_INVALID", str(error))
        self.assertEqual("SCHEMA_INVALID", error.errors[0]["code"])


if __name__ == "__main__":
    unittest.main()
