from pydantic import BaseSettings, Field
from config.metaclasses import Singleton
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.engine import create_engine
from typing import Union


class Settings(BaseSettings):
    """Base settings class"""

    __metaclass__ = Singleton

    db_name: str = Field(env="DB_NAME")
    db_host: str = Field(env="DB_HOST")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")
    application_host: str = Field(env="APPLICATION_HOST")
    password_salt: str = Field(env="SALT")

    @property
    def db_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"

    class Config:
        env_file = ".env"


settings = Settings()


class DBSession:
    """
    Handles base db configuration and session access in repos \n
    `get_session` method returns session for performing db operations
    """

    _session = sessionmaker(bind=create_engine(settings.db_string))
    base = declarative_base()

    def get_session(self) -> Union[Session, None]:
        session = self._session()
        try:
            return session
        except:
            session.rollback()
        finally:
            session.close()


POSSIBLE_PERMS = (
    "view_user",
    "manage_user",
    "view_order",
    "manage_order",
    "view_product",
    "manage_product",
    "manage_group",
    "view_group",
)
