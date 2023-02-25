from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.users.infrastructure.repositories import UserRepository
from modules.users.application.handlers import UserHandler
from modules.users.application.dto import RegisterUserDTO, UserDTO


users_router = router = APIRouter()


@router.post("/create-user")
async def create_user(dto: RegisterUserDTO):
    repo = UserHandler(repo=UserRepository())
    response = repo.add_user(dto)
    return response