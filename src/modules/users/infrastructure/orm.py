from config.settings import DBSession
from modules.users.domain import models, value_objects
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import mapper


class User(DBSession.base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(LargeBinary)
    group = Column(String)


mapper(models.User, User)