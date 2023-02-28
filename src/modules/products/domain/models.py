from dataclasses import dataclass
from base.types import Entity
from decimal import Decimal
from datetime import datetime
from enum import Enum
from typing import Optional


class Status(Enum):
    accepted = "accepted"
    declined = "declined"
    sent = "sent"
    paid = "paid"


class Currency(Enum):
    usd = "usd"
    eur = "eur"
    pln = "pln"


@dataclass
class Product(Entity):
    owner_id: int
    name: str
    price: Decimal
    currency: Currency
    id: Optional[int] = None

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)


@dataclass
class Order(Entity):
    user_id: int
    product_id: int
    date: datetime
    status: Status
    id: Optional[int] = None

    def update_data(self, dto):
        for field in self.__dict__.keys():
            if field in ["_sa_instance_state", "password"]:
                continue

            new_value = getattr(dto, field)
            setattr(self, field, new_value)

    def check_possibility_to_delete(self):
        if (datetime.today()-self.date).days >= 1:
            raise ValueError("Time to cancel order passed!")

