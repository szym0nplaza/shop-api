from pydantic import BaseModel


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
    password: str

class UpdatePasswordDTO(BaseModel):
    id: int
    new_password: str