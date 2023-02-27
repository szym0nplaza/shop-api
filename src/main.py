from fastapi import FastAPI
from modules.users.presentation.routers import users_router
from modules.products.presentation.routers import products_router, orders_router


app = FastAPI()
app.include_router(users_router, prefix="/api", tags=["Users API"])
app.include_router(products_router, prefix="/api", tags=["Products API"])
app.include_router(orders_router, prefix="/api", tags=["Orders API"])
