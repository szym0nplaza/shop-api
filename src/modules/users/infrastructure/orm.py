from config.settings import DBSession
from modules.users.domain import models, value_objects
from sqlalchemy import Column, Integer, String, LargeBinary, ARRAY, ForeignKey
from sqlalchemy.orm import mapper, relationship


class Group(DBSession.base):
    __tablename__ = "groups"

    name = Column(String, primary_key=True, unique=True)
    perms = Column(String)


class User(DBSession.base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(LargeBinary)
    stripe_id = Column(String, nullable=True)
    group = Column(String, ForeignKey(Group.name), nullable=True)


mapper(models.User, User)
mapper(models.Group, Group)