from .intefraces import IUserRepository, IAuthModule
from modules.users.domain.models import User
from modules.users.domain.value_objects import Password
from .dto import RegisterUserDTO, UserDTO, UpdateUserDTO, ChangePasswordDTO, LoginDTO, GroupDTO
from config.settings import POSSIBLE_PERMS
from typing import List


class UserHandler:
    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo

    def add_user(self, dto: RegisterUserDTO) -> UserDTO:
        with self._repo:
            user = User(
                email=dto.email,
                name=dto.name,
                surname=dto.surname,
                password=Password(dto.password).hashed_value,
                group=dto.group
            )
            self._repo.add_user(user)
            user = self._repo.get_user_by_email(dto.email)
            return UserDTO(**user.__dict__)

    def get_user(self, id: int) -> UserDTO:
        with self._repo:
            result = self._repo.get_user(id)
            return UserDTO(**result.__dict__)
    
    def update_user(self, dto: UpdateUserDTO) -> UserDTO:
        with self._repo:
            user: User = self._repo.get_user(dto.id)
            user.update_data(dto)
            user = self._repo.get_user_by_email(dto.email)
            return UserDTO(**user.__dict__)

    def change_password(self, dto: ChangePasswordDTO) -> None:
        with self._repo:
            user: User = self._repo.get_user(dto.id)
            user.change_password(dto.new_password)


class AuthHandler:
    def __init__(self, repo: IUserRepository, auth: IAuthModule) -> None:
        self._repo = repo
        self._auth = auth

    def check_password(self, dto: LoginDTO) -> bool:
        with self._repo:
            user: User = self._repo.get_user_by_email(dto.email)
            return user.check_passwords(dto.given_password)
        
    def login(self, dto: LoginDTO):
        tokens = self._auth.create_tokens(dto.email)
        return tokens
    
    def get_groups(self) -> List[GroupDTO]:
        with self._repo:
            qs = self._repo.get_groups()
            results = [GroupDTO(name=record.name, perms=record.perms.split(",")) for record in qs]
            return results

    def get_perms(self) -> tuple:
        return POSSIBLE_PERMS
    
    def modify_group(self, dto: GroupDTO):
        with self._repo:
            group = self._repo.get_group_by_name(dto.name)
            group.perms = ",".join(dto.perms)
