from dataclasses import dataclass
from base.types import Entity
from typing import Optional
from .value_objects import Password
from typing import Union


@dataclass
class Group(Entity):
    name: str
    perms: str


@dataclass
class User(Entity):
    email: str  # Later we should add value object for this
    name: str
    surname: str
    password: Union[str, bytes]
    group: str
    stripe_id: Optional[str] = None
    id: Optional[int] = None

    def change_password(self, new_password: str):
        _hashed_password = Password(value=new_password).hashed_value
        if self.password == _hashed_password:
            raise ValueError("Passwords are the same!")
        self.password = _hashed_password

    def check_passwords(self, given_password: str):
        _hashed_password = Password(value=given_password).hashed_value
        return self.password == _hashed_password

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password", "stripe_id"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"