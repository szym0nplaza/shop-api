from fastapi import FastAPI
from modules.users.presentation.routers import users_router
from modules.products.presentation.routers import products_router, orders_router, payments_router
from config.settings import settings
import uvicorn


app = FastAPI()
app.include_router(users_router, prefix="/api", tags=["Users API"])
app.include_router(products_router, prefix="/api", tags=["Products API"])
app.include_router(orders_router, prefix="/api", tags=["Orders API"])
app.include_router(payments_router, prefix="/api", tags=["Payment API"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.application_host,
        log_level="debug",
        reload=True,
        port=8000,
    )