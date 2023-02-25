from abc import ABC, abstractmethod
from modules.users.domain.models import User
from typing import Tuple


class IUserRepository(ABC):
    def __enter__(self):
        pass

    def __exit__(self, *__args) -> None:
        pass

    @abstractmethod
    def add_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        raise NotImplementedError


class IAuthModule(ABC):
    @abstractmethod
    def create_tokens(self, email: str) -> Tuple[str, str]:
        raise NotImplementedError
