from copy import deepcopy
from dataclasses import dataclass

from validator.semantic_validator import validateMessage

from .errors import PasspodValidationError


@dataclass(frozen=True)
class Message:
    _data: dict

    def __init__(
        self,
        messageIdentity=None,
        handshakeIdentity=None,
        messageType=None,
        sender=None,
        parentReference=None,
        recipient=None,
        timestamp=None,
        profileAssociation=None,
        versionAssociation=None,
        evidenceReferences=None,
        extensions=None,
    ):
        data = {
            "messageIdentity": deepcopy(messageIdentity),
            "handshakeIdentity": deepcopy(handshakeIdentity),
            "messageType": deepcopy(messageType),
            "sender": deepcopy(sender),
        }

        optional = {
            "parentReference": parentReference,
            "recipient": recipient,
            "timestamp": timestamp,
            "profileAssociation": profileAssociation,
            "versionAssociation": versionAssociation,
            "evidenceReferences": evidenceReferences,
            "extensions": extensions,
        }

        for key, value in optional.items():
            if value is not None:
                data[key] = deepcopy(value)

        object.__setattr__(self, "_data", data)
        self.validate()

    def __repr__(self):
        return (
            "Message("
            f"message_identity={self.message_identity!r}, "
            f"message_type={self.message_type!r}, "
            f"handshake_identity={self.handshake_identity!r}"
            ")"
        )

    @classmethod
    def from_mapping(cls, mapping):
        instance = cls.__new__(cls)
        object.__setattr__(instance, "_data", deepcopy(dict(mapping)))
        instance.validate()
        return instance

    @property
    def message_identity(self):
        return deepcopy(self._data.get("messageIdentity"))

    @property
    def handshake_identity(self):
        return deepcopy(self._data.get("handshakeIdentity"))

    @property
    def message_type(self):
        return deepcopy(self._data.get("messageType"))

    @property
    def parent_reference(self):
        return deepcopy(self._data.get("parentReference"))

    @property
    def sender(self):
        return deepcopy(self._data.get("sender"))

    @property
    def recipient(self):
        return deepcopy(self._data.get("recipient"))

    def to_mapping(self):
        return deepcopy(self._data)

    def validate(self):
        result = validateMessage(self.to_mapping())
        if not result.get("valid"):
            raise PasspodValidationError("validateMessage", result.get("errors", []))
        return result
