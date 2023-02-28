from abc import ABC, abstractmethod
from modules.users.domain.models import User, Group
from typing import Tuple, List


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
    
    @abstractmethod
    def get_groups(self) -> List[Group]:
        raise NotImplementedError
    
    @abstractmethod
    def get_group_by_name(self, name: str) -> Group:
        raise NotImplementedError


class IAuthModule(ABC):
    @abstractmethod
    def create_tokens(self, email: str) -> Tuple[str, str]:
        raise NotImplementedError


class IPaymentGateway(ABC):
    @abstractmethod
    def create_seller_acc(self, user: User):
        raise NotImplementedError
