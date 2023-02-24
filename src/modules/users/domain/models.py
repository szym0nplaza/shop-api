from dataclasses import dataclass
from base.types import Entity
from typing import Optional
from .value_objects import Password
from typing import Union


@dataclass
class User(Entity):
    email: str  # Later we should add value object for this
    name: str
    surname: str
    password: Union[str, bytes]
    group: str
    id: Optional[int] = None

    def change_password(self, new_password: str):
        _hashed_password = Password(value=new_password).hashed_value
        if self.password == _hashed_password:
            raise ValueError("Passwords are the same!")
        self.password = _hashed_password 

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)