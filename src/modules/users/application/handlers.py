from .intefraces import IUserRepository
from modules.users.domain.models import User
from modules.users.domain.value_objects import Password
from .dto import RegisterUserDTO, UserDTO, UpdateUserDTO, UpdatePasswordDTO


class UserHandler:
    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo

    def add_user(self, dto: RegisterUserDTO) ->UserDTO:
        with self._repo:
            user = User(
                email=dto.email,
                name=dto.name,
                surname=dto.surname,
                password=Password(dto.password).hashed_value,
                group=dto.group
            )
            self._repo.add_user(user)
        return UserDTO(**user.__dict__)

    def get_user(self, id: int) -> UserDTO:
        with self._repo:
            result = self._repo.get_user(id)
        return UserDTO(**result.__dict__)
    
    def update_user(self, dto: UpdateUserDTO) -> None:
        with self._repo:
            user: User = self._repo.get_user(dto.id)
            user.update_data(dto)

    def change_password(self, dto: UpdatePasswordDTO) -> None:
        with self._repo:
            user: User = self._repo.get_user(dto.id)
            user.change_password(dto.new_password)