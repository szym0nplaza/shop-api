from dataclasses import dataclass
from base.types import Entity
from decimal import Decimal
from datetime import datetime
from enum import Enum


class Status(Enum):
    accepted = "accepted"
    declined = "declined"
    sent = "sent"
    paid = "paid"


@dataclass
class Product(Entity):
    id: int
    owner_id: int
    name: str
    price: Decimal

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)


@dataclass
class Order(Entity):
    id: int
    user_id: int
    product_id: int
    date: datetime
    status: Status

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)

