from modules.users.application.intefraces import IUserRepository
from modules.users.domain.models import User, Group
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from config.settings import DBSession
from typing import List


class UserRepository(IUserRepository):
    def __init__(self, session_class=DBSession()) -> None:
        self._session_class = session_class

    def __enter__(self) -> None:
        self._session: Session = self._session_class.get_session()

    def __exit__(self, *__args):
        try:
            self._session.commit()
        except:
            self._session.rollback()
        finally:
            self._session.close()

    def add_user(self, user: User) -> User:
        return self._session.add(user)
    
    def get_user(self, id: int) -> User:
        result = self._session.query(User).filter_by(id=id).first()
        return result
    
    def get_user_by_email(self, email: str) -> User:
        result = self._session.query(User).filter_by(email=email).first()
        return result
    
    def get_groups(self) -> List[Group]:
        result = self._session.query(Group).all()
        return result
    
    def get_group_by_name(self, name: str) -> Group:
        result = self._session.query(Group).filter_by(name=name).first()
        return result
