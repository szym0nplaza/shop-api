from modules.users.application.intefraces import IUserRepository, IAuthModule
from modules.users.domain.models import User, Group
from typing import List


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


ids = id_generator()


class MockAuthModule(IAuthModule):
    def create_tokens(self, email: str):
        pass


class MockUserRepo(IUserRepository):
    _users_db = []
    _groups_db = [Group(name="admin", perms="__all__")]

    def __enter__(self):
        pass

    def __exit__(self, *__args) -> None:
        pass

    def add_user(self, user: User) -> None:
        user.id = next(ids)
        self._users_db.append(user)

    def get_user(self, id: int) -> User:
        return tuple(filter(lambda record: record.id == id, self._users_db))[0]

    def get_user_by_email(self, email: str) -> User:
        return tuple(filter(lambda record: record.email == email, self._users_db))[0]
    
    def get_groups(self) -> List[Group]:
        return self._groups_db
    
    def get_group_by_name(self, name: str) -> Group:
        result = tuple(filter(lambda x: x.name == name, self._groups_db))[0]
        return result
