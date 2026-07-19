from copy import deepcopy
from dataclasses import dataclass

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
        if self._data.get("messages"):
            self.validate()

    @classmethod
    def from_mapping(cls, mapping):
        instance = cls.__new__(cls)
        object.__setattr__(instance, "_data", deepcopy(dict(mapping)))
        if instance._data.get("messages"):
            instance.validate()
        return instance

    @property
    def handshake_identity(self):
        return deepcopy(self._data.get("handshakeIdentity"))

    @property
    def history(self):
        return tuple(Message.from_mapping(message) for message in self._data.get("messages", []))

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

    def to_mapping(self):
        return deepcopy(self._data)

    def validate(self):
        if not self._data.get("messages"):
            return {"valid": True, "errors": []}

        result = validateHandshake(self.to_mapping())
        if not result.get("valid"):
            raise PasspodValidationError("validateHandshake", result.get("errors", []))
        return result


def _message_mapping(message):
    if isinstance(message, Message):
        return message.to_mapping()
    return deepcopy(dict(message))
