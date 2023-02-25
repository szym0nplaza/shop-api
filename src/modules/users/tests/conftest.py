from modules.users.application.intefraces import IUserRepository
from modules.users.domain.models import User


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


ids = id_generator()


class MockUserRepo(IUserRepository):
    _db = []

    def __enter__(self):
        pass

    def __exit__(self, *__args) -> None:
        pass

    def add_user(self, user: User) -> None:
        user.id = next(ids)
        self._db.append(user)

    def get_user(self, id: int) -> User:
        return tuple(filter(lambda record: record.id == id, self._db))[0]

    def get_user_by_email(self, email: str) -> User:
        return tuple(filter(lambda record: record.email == email, self._db))[0]
