from fastapi import APIRouter, Security
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from base.auth import check_access
from modules.products.application.dto import (
    ProductDTO,
    CreateProductDTO,
    OrderDTO,
    CreateOrderDTO,
    PaymentDTO,
)
from modules.products.application.handlers import (
    ProductHandler,
    OrderHandler,
    PaymentHandler,
)
from modules.products.infrastructure.repositories import (
    ProductRepository,
    OrderRepository,
)
from modules.products.infrastructure.ext import PaymentGateway
from modules.users.infrastructure.repositories import UserRepository
from typing import List


products_router = APIRouter()
orders_router = APIRouter()
payments_router = APIRouter()


@products_router.post("/create-product")
async def create_product(dto: CreateProductDTO):
    handler = ProductHandler(repo=ProductRepository())
    handler.add_product(dto)
    return JSONResponse({"message": "created"}, status_code=201)


@products_router.get(
    "/products",
    response_model=List[ProductDTO],
    dependencies=[Security(check_access, scopes=["view_product"])],
)
async def get_products():
    handler = ProductHandler(repo=ProductRepository())
    response = handler.get_products()
    return response


@products_router.get(
    "/products/{id}",
    response_model=ProductDTO,
    dependencies=[Security(check_access, scopes=["view_product"])],
)
async def get_product(id: int):
    handler = ProductHandler(repo=ProductRepository())
    response = handler.get_product(id)
    return response


@products_router.get(
    "/seller-products/{seller_id}",
    response_model=List[ProductDTO],
    dependencies=[Security(check_access, scopes=["view_product"])],
)
async def get_seller_product(seller_id: int):
    handler = ProductHandler(repo=ProductRepository())
    response = handler.get_seller_products(seller_id)
    return response


@products_router.patch(
    "/products",
    dependencies=[Security(check_access, scopes=["manage_product"])],
)
async def update_product(dto: ProductDTO):
    handler = ProductHandler(repo=ProductRepository())
    handler.udpate_product(dto)
    return JSONResponse({"message": "Product updated"}, status_code=200)


@products_router.delete(
    "/products/{id}",
    dependencies=[Security(check_access, scopes=["manage_product"])],
)
async def delete_product(id: int):
    handler = ProductHandler(repo=ProductRepository())
    handler.delete_product(id)
    return JSONResponse({"message": "Product deleted."}, status_code=200)


##########################################


@orders_router.post("/create-order")
async def create_order(dto: CreateOrderDTO):
    handler = OrderHandler(repo=OrderRepository())
    handler.add_order(dto)
    return JSONResponse({"message": "created"}, status_code=201)


@orders_router.get("/orders/{user_id}", response_model=List[OrderDTO])
async def get_orders(user_id: int):
    handler = OrderHandler(repo=OrderRepository())
    result = handler.get_orders(user_id)
    return result


@orders_router.get("/orders/{id}", response_model=OrderDTO)
async def get_order(id: int):
    handler = OrderHandler(repo=OrderRepository())
    result = handler.get_order(id)
    return result


@orders_router.patch("/orders")
async def update_order(dto: OrderDTO):
    handler = OrderHandler(repo=OrderRepository())
    try:
        handler.udpate_order(dto)
    except ValueError as e:
        return JSONResponse({"detail": str(e)}, status_code=422)
    return JSONResponse({"message": "Order updated"}, status_code=200)


@orders_router.delete("/orders/{id}")
async def delete_order(id: int):
    handler = OrderHandler(repo=OrderRepository())
    try:
        handler.delete_order(id)
    except ValueError as e:
        return JSONResponse({"detail": str(e)}, status_code=422)
    return JSONResponse({"message": "Order updated"}, status_code=200)


##########################################


@payments_router.post("proceed-payment")
async def create_payment(dto: PaymentDTO):
    handler = PaymentHandler(
        product_repo=ProductRepository(),
        order_repo=OrderRepository(),
        user_repo=UserRepository(),
        payments=PaymentGateway(),
    )
    handler.handle_payment(dto)
    return JSONResponse({"message": "Order updated"}, status_code=200)
