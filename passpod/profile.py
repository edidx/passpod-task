from copy import deepcopy
from dataclasses import dataclass

from validator.semantic_validator import validateProfile

from .errors import PasspodValidationError


@dataclass(frozen=True)
class Profile:
    _data: dict

    def __init__(
        self,
        profileIdentity=None,
        profileVersion=None,
        lifecycle=None,
        metadata=None,
        mayDefine=None,
        mustNotRedefine=None,
        extensions=None,
    ):
        data = {
            "profileIdentity": deepcopy(profileIdentity),
            "profileVersion": deepcopy(profileVersion),
            "lifecycle": deepcopy(lifecycle),
        }

        optional = {
            "metadata": metadata,
            "mayDefine": mayDefine,
            "mustNotRedefine": mustNotRedefine,
            "extensions": extensions,
        }

        for key, value in optional.items():
            if value is not None:
                data[key] = deepcopy(value)

        object.__setattr__(self, "_data", data)
        self.validate()

    @classmethod
    def from_mapping(cls, mapping):
        instance = cls.__new__(cls)
        object.__setattr__(instance, "_data", deepcopy(dict(mapping)))
        instance.validate()
        return instance

    @property
    def profile_identity(self):
        return deepcopy(self._data.get("profileIdentity"))

    @property
    def profile_version(self):
        return deepcopy(self._data.get("profileVersion"))

    @property
    def lifecycle(self):
        return deepcopy(self._data.get("lifecycle"))

    def to_mapping(self):
        return deepcopy(self._data)

    def validate(self):
        result = validateProfile(self.to_mapping())
        if not result.get("valid"):
            raise PasspodValidationError("validateProfile", result.get("errors", []))
        return result

