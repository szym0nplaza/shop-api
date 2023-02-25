from modules.users.application.intefraces import IUserRepository
from modules.users.domain.models import User
from sqlalchemy.orm import Session
from config.settings import DBSession


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
