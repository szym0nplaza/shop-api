from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class CreateProductDTO(BaseModel):
    id: int
    owner_id: int
    name: str
    price: Decimal

class ProductDTO(BaseModel):
    id: int
    name: str
    price: Decimal

class OrderDTO(BaseModel):
    id: int
    user_id: int
    product_id: int
    date: datetime
    status: str