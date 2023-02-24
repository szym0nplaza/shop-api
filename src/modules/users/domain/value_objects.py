from dataclasses import dataclass
from base.types import ValueObject
from config.settings import settings
import hashlib
import re

PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}"


@dataclass
class Password(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not re.match(PASSWORD_REGEX, self.value):
            raise ValueError(
                "Password must contain at least 8 characters,\
                1 letter, 1 number and 1 special character!"
            )
        self.hashed_value = hashlib.pbkdf2_hmac(
            "sha256", self.value.encode("utf-8"), settings.password_salt.encode("utf-8"), 10000, 32
        )

    def __eq__(self, __o: object) -> bool:
        return self.hashed_value == __o
