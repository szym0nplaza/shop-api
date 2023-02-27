from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class CreateProductDTO(BaseModel):
    owner_id: int
    name: str
    price: Decimal

class ProductDTO(BaseModel):
    id: int
    name: str
    price: Decimal
    owner_id: int

class OrderDTO(BaseModel):
    id: int
    user_id: int
    product_id: int
    date: datetime
    status: str

class CreateOrderDTO(BaseModel):
    user_id: int
    product_id: int
    date: datetime
    status: str