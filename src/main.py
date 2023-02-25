from fastapi import FastAPI
from modules.users.presentation.routers import users_router


app = FastAPI()
app.include_router(users_router, prefix="/api", tags=["Users API"])
