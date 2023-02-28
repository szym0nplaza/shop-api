from config.settings import DBSession
from modules.products.domain import models
from modules.users.infrastructure.orm import User
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import mapper


class Product(DBSession.base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey(User.id))
    name = Column(String)
    price = Column(DECIMAL(precision=15, scale=2))
    currency = Column(String)


class Order(DBSession.base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    date = Column(DateTime)
    status = Column(String)


mapper(models.Product, Product)
mapper(models.Order, Order)
