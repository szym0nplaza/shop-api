from abc import ABC, abstractmethod
from modules.users.domain.models import User
from .dto import UpdateUserDTO


class IUserRepository(ABC):
    def __enter__(self):
        pass

    def __exit__(self, *__args) -> None:
        pass

    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user(self, id: int) -> User:
        pass

