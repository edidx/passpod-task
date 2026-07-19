class PasspodValidationError(ValueError):
    """SDK-facing validation failure with deterministic validator errors."""

    def __init__(self, operation, errors):
        self.operation = operation
        self.errors = tuple(_copy_error(error) for error in errors)
        super().__init__(self._summary())

    def _summary(self):
        if not self.errors:
            return f"{self.operation} failed validation"

        codes = ", ".join(error.get("code", "UNKNOWN") for error in self.errors)
        return f"{self.operation} failed validation: {codes}"


def _copy_error(error):
    if isinstance(error, dict):
        return dict(error)
    return {"code": "UNKNOWN", "path": "$", "message": str(error)}

