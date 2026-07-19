import unittest
from dataclasses import FrozenInstanceError

from passpod import Handshake, Message, PasspodValidationError, Profile


def error_codes(error):
    return [entry["code"] for entry in error.errors]


class MessageTests(unittest.TestCase):
    def test_valid_message_construction(self):
        message = Message(
            messageIdentity="msg-1",
            handshakeIdentity="hs-1",
            messageType="PROPOSE",
            sender="participant-alpha",
        )

        self.assertEqual("msg-1", message.message_identity)
        self.assertEqual("hs-1", message.handshake_identity)
        self.assertEqual("PROPOSE", message.message_type)

    def test_construction_from_mapping(self):
        message = Message.from_mapping(
            {
                "messageIdentity": "msg-1",
                "handshakeIdentity": "hs-1",
                "messageType": "PROPOSE",
                "sender": "participant-alpha",
            }
        )

        self.assertEqual("participant-alpha", message.sender)

    def test_mapping_round_trip(self):
        data = {
            "messageIdentity": "msg-1",
            "handshakeIdentity": "hs-1",
            "messageType": "PROPOSE",
            "sender": "participant-alpha",
            "recipient": "participant-beta",
            "evidenceReferences": ["ev-1"],
        }
        message = Message.from_mapping(data)

        self.assertEqual(data, message.to_mapping())

    def test_validation_failure(self):
        with self.assertRaises(PasspodValidationError) as raised:
            Message.from_mapping(
                {
                    "messageIdentity": "msg-1",
                    "handshakeIdentity": "hs-1",
                    "messageType": "UNKNOWN",
                    "sender": "participant-alpha",
                }
            )

        self.assertIn("SCHEMA_INVALID", error_codes(raised.exception))

    def test_attempted_direct_mutation(self):
        message = Message("msg-1", "hs-1", "PROPOSE", "participant-alpha")

        with self.assertRaises(FrozenInstanceError):
            message._data = {}

    def test_external_mapping_mutation_does_not_alter_state(self):
        data = {
            "messageIdentity": "msg-1",
            "handshakeIdentity": "hs-1",
            "messageType": "PROPOSE",
            "sender": {"id": "participant-alpha"},
            "evidenceReferences": ["ev-1"],
        }
        message = Message.from_mapping(data)

        data["sender"]["id"] = "changed"
        data["evidenceReferences"].append("ev-2")
        exported = message.to_mapping()
        exported["sender"]["id"] = "changed-again"

        self.assertEqual({"id": "participant-alpha"}, message.sender)
        self.assertEqual(["ev-1"], message.to_mapping()["evidenceReferences"])


class HandshakeTests(unittest.TestCase):
    def msg(self, identity, message_type, parent=None, handshake_identity="hs-1"):
        data = {
            "messageIdentity": identity,
            "handshakeIdentity": handshake_identity,
            "messageType": message_type,
            "sender": "participant-alpha",
        }
        if parent is not None:
            data["parentReference"] = parent
        return Message.from_mapping(data)

    def test_creation_with_handshake_identity(self):
        handshake = Handshake("hs-1")

        self.assertEqual("hs-1", handshake.handshake_identity)
        self.assertEqual("not_started", handshake.lifecycle)
        self.assertFalse(handshake.is_closed)
        self.assertEqual(0, len(handshake.history))

    def test_creation_from_minimal_valid_propose(self):
        handshake = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])

        self.assertEqual("hs-1", handshake.handshake_identity)
        self.assertEqual("proposed", handshake.lifecycle)
        self.assertFalse(handshake.is_closed)
        self.assertEqual(1, len(handshake.history))

    def test_append_challenge_agree_close_and_states(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])
        challenged = proposed.append(self.msg("msg-2", "CHALLENGE", parent="msg-1"))
        agreed = challenged.append(self.msg("msg-3", "AGREE", parent="msg-2"))
        closed = agreed.append(self.msg("msg-4", "CLOSE", parent="msg-3"))

        self.assertEqual("proposed", proposed.lifecycle)
        self.assertEqual("challenged", challenged.lifecycle)
        self.assertEqual("agreed", agreed.lifecycle)
        self.assertEqual("closed", closed.lifecycle)
        self.assertTrue(closed.is_closed)

    def test_append_returns_new_handshake_and_preserves_prior_history(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])
        challenged = proposed.append(self.msg("msg-2", "CHALLENGE", parent="msg-1"))

        self.assertIsNot(proposed, challenged)
        self.assertEqual(1, len(proposed.history))
        self.assertEqual(2, len(challenged.history))

    def test_invalid_transition_is_rejected(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])

        with self.assertRaises(PasspodValidationError) as raised:
            proposed.append(self.msg("msg-2", "AGREE", parent="msg-1"))

        self.assertIn("INVALID_TRANSITION", error_codes(raised.exception))
        self.assertEqual(1, len(proposed.history))

    def test_missing_parent_is_rejected(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])

        with self.assertRaises(PasspodValidationError) as raised:
            proposed.append(self.msg("msg-2", "CHALLENGE"))

        self.assertIn("PARENT_REQUIRED", error_codes(raised.exception))

    def test_duplicate_message_identity_is_rejected(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])

        with self.assertRaises(PasspodValidationError) as raised:
            proposed.append(self.msg("msg-1", "CHALLENGE", parent="msg-1"))

        self.assertIn("DUPLICATE_MESSAGE_ID", error_codes(raised.exception))

    def test_mismatched_handshake_identity_is_rejected(self):
        proposed = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])

        with self.assertRaises(PasspodValidationError) as raised:
            proposed.append(self.msg("msg-2", "CHALLENGE", parent="msg-1", handshake_identity="other"))

        self.assertIn("HANDSHAKE_ID_MISMATCH", error_codes(raised.exception))

    def test_message_after_close_is_rejected(self):
        closed = (
            Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])
            .append(self.msg("msg-2", "CHALLENGE", parent="msg-1"))
            .append(self.msg("msg-3", "AGREE", parent="msg-2"))
            .append(self.msg("msg-4", "CLOSE", parent="msg-3"))
        )

        with self.assertRaises(PasspodValidationError) as raised:
            closed.append(self.msg("msg-5", "CHALLENGE", parent="msg-4"))

        self.assertIn("MESSAGE_AFTER_CLOSE", error_codes(raised.exception))

    def test_history_cannot_be_externally_reordered_or_modified(self):
        handshake = Handshake("hs-1", messages=[self.msg("msg-1", "PROPOSE")])
        history = handshake.history

        with self.assertRaises(AttributeError):
            history.append(self.msg("msg-2", "CHALLENGE", parent="msg-1"))

        exported = handshake.to_mapping()
        exported["messages"].clear()

        self.assertEqual(1, len(handshake.history))
        self.assertEqual("msg-1", handshake.history[0].message_identity)


class ProfileTests(unittest.TestCase):
    def test_valid_minimal_profile_construction(self):
        profile = Profile("profile-1", "0.1", "draft")

        self.assertEqual("profile-1", profile.profile_identity)
        self.assertEqual("0.1", profile.profile_version)
        self.assertEqual("draft", profile.lifecycle)

    def test_mapping_round_trip(self):
        data = {
            "profileIdentity": "profile-1",
            "profileVersion": "0.1",
            "lifecycle": "draft",
            "metadata": {"name": "Minimal"},
        }
        profile = Profile.from_mapping(data)

        self.assertEqual(data, profile.to_mapping())

    def test_core_semantic_redefinition_is_rejected(self):
        with self.assertRaises(PasspodValidationError) as raised:
            Profile.from_mapping(
                {
                    "profileIdentity": "profile-invalid",
                    "profileVersion": "0.1",
                    "lifecycle": "draft",
                    "mayDefine": {
                        "terminology": {
                            "PROPOSE": "Invalid redefinition"
                        }
                    },
                }
            )

        self.assertIn("CORE_SEMANTIC_REDEFINITION", error_codes(raised.exception))

    def test_attempted_direct_mutation(self):
        profile = Profile("profile-1", "0.1", "draft")

        with self.assertRaises(FrozenInstanceError):
            profile._data = {}


class ValidatorConsumptionTests(unittest.TestCase):
    def test_message_validation_uses_existing_validator(self):
        with self.assertRaises(PasspodValidationError) as raised:
            Message.from_mapping(
                {
                    "messageIdentity": "msg-1",
                    "handshakeIdentity": "hs-1",
                    "messageType": "PROPOSE",
                }
            )

        self.assertEqual("validateMessage", raised.exception.operation)
        self.assertIn("SCHEMA_INVALID", error_codes(raised.exception))


if __name__ == "__main__":
    unittest.main()
