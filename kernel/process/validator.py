from .process import Process
from .exceptions import InvalidProcessNameError, ProcessAlreadyExistsError

class ProcessValidator:
    FORBIDDEN_CHARACTERS = {"@", "$", "!", "%", "^", "&", "*"}
    MAX_NAME_LENGTH = 100

    def __init__(self, *, name: str, processes: list[Process]):
        self.name = name
        self.processes = processes

    def validate_name_type(self):
        if not isinstance(self.name, str):
            raise InvalidProcessNameError("Process name must be a string.")

    def validate_name_length(self):
        if len(self.name) > self.MAX_NAME_LENGTH:
            raise InvalidProcessNameError(
                f"Process name must be less than {self.MAX_NAME_LENGTH} characters."
            )
        if not self.name.strip():
            raise InvalidProcessNameError("Process name cannot be empty or whitespace only.")

    def validate_forbidden_characters(self):
        found = [c for c in self.name if c in self.FORBIDDEN_CHARACTERS]
        if found:
            raise InvalidProcessNameError(
                f"Process name contains forbidden characters: {found}."
            )

    def validate_unique_name(self):
        if any(p.name == self.name for p in self.processes):
            raise ProcessAlreadyExistsError(f"Process name '{self.name}' already exists.")

    def validate(self):
        self.validate_name_type()
        self.validate_name_length()
        self.validate_forbidden_characters()
        self.validate_unique_name()

