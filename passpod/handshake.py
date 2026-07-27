from copy import deepcopy
from dataclasses import dataclass
import json

from validator.semantic_validator import validateHandshake

from .errors import PasspodValidationError
from .message import Message


MESSAGE_STATE = {
    "PROPOSE": "proposed",
    "CHALLENGE": "challenged",
    "AGREE": "agreed",
    "CLOSE": "closed",
}


@dataclass(frozen=True)
class Handshake:
    _data: dict

    def __init__(
        self,
        handshakeIdentity=None,
        messages=None,
        lifecycle=None,
        terminalClosure=None,
        parentRelationships=None,
        profileAssociation=None,
        versionAssociation=None,
        extensions=None,
    ):
        data = {
            "handshakeIdentity": deepcopy(handshakeIdentity),
            "messages": [_message_mapping(message) for message in (messages or [])],
        }

        optional = {
            "lifecycle": lifecycle,
            "terminalClosure": terminalClosure,
            "parentRelationships": parentRelationships,
            "profileAssociation": profileAssociation,
            "versionAssociation": versionAssociation,
            "extensions": extensions,
        }

        for key, value in optional.items():
            if value is not None:
                data[key] = deepcopy(value)

        object.__setattr__(self, "_data", data)
        self._set_history()
        self.validate()

    def __repr__(self):
        return (
            "Handshake("
            f"handshake_identity={self.handshake_identity!r}, "
            f"state={self.lifecycle!r}, "
            f"message_count={self.message_count!r}"
            ")"
        )

    @classmethod
    def from_mapping(cls, mapping):
        instance = cls.__new__(cls)
        object.__setattr__(instance, "_data", deepcopy(dict(mapping)))
        instance._set_history()
        instance.validate()
        return instance

    def _set_history(self):
        object.__setattr__(
            self,
            "_history",
            tuple(Message.from_mapping(message) for message in self._data.get("messages", [])),
        )

    @property
    def handshake_identity(self):
        return deepcopy(self._data.get("handshakeIdentity"))

    @property
    def history(self):
        return self._history

    @property
    def message_count(self):
        return len(self._history)

    @property
    def last_message(self):
        if not self._history:
            return None
        return self._history[-1]

    @property
    def lifecycle(self):
        explicit = self._data.get("lifecycle")
        if explicit is not None:
            return explicit

        messages = self._data.get("messages", [])
        if not messages:
            return "not_started"

        return MESSAGE_STATE.get(messages[-1].get("messageType"), "not_started")

    @property
    def is_closed(self):
        if self.lifecycle == "closed":
            return True

        messages = self._data.get("messages", [])
        return bool(messages and messages[-1].get("messageType") == "CLOSE")

    def append(self, message):
        candidate = self.to_mapping()
        candidate.setdefault("messages", [])
        candidate["messages"].append(_message_mapping(message))
        return self.from_mapping(candidate)

    def get_message(self, message_identity):
        expected = _identity_key(message_identity)
        for message in self._history:
            if _identity_key(message.message_identity) == expected:
                return message
        return None

    def to_mapping(self):
        return deepcopy(self._data)

    def validate(self):
        result = validateHandshake(self.to_mapping())
        if not result.get("valid"):
            raise PasspodValidationError("validateHandshake", result.get("errors", []))
        return result


def _message_mapping(message):
    if isinstance(message, Message):
        return message.to_mapping()
    return deepcopy(dict(message))


def _identity_key(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))
