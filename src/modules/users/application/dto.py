from pydantic import BaseModel
from typing import List


class RegisterUserDTO(BaseModel):
    email: str
    name: str
    surname: str
    group: str
    password: str


class UserDTO(BaseModel):
    id: int
    email: str
    name: str
    surname: str
    group: str


class UpdateUserDTO(BaseModel):
    id: int
    email: str
    name: str
    surname: str
    group: str


class ChangePasswordDTO(BaseModel):
    id: int
    new_password: str


class LoginDTO(BaseModel):
    email: str
    given_password: str


class GroupDTO(BaseModel):
    name: str
    perms: List[str]
