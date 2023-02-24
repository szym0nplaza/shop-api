from config.settings import DBSession
from modules.users.domain import models, value_objects
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm.mapper import Mapper


class User(DBSession.base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(LargeBinary)
    group = Column(String)


Mapper(models.User, User)