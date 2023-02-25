from fastapi import APIRouter
from fastapi.responses import JSONResponse
from modules.users.infrastructure.repositories import UserRepository
from modules.users.infrastructure.auth import AuthModule
from modules.users.application.handlers import UserHandler, AuthHandler
from modules.users.application.dto import (
    RegisterUserDTO,
    UserDTO,
    UpdateUserDTO,
    ChangePasswordDTO,
    LoginDTO
)


users_router = router = APIRouter()


@router.post("/login")
async def login(dto: LoginDTO):
    auth_handler = AuthHandler(repo=UserRepository(), auth=AuthModule())
    auth_handler.check_password(dto)
    access_token, refresh_token = auth_handler.login(dto)
    response = JSONResponse({"message": "Successfully logged in."})
    response.set_cookie(key="access_token", value=access_token)
    response.set_cookie(key="refresh_token", value=refresh_token)
    return response


@router.get("/get-user/{id}", response_model=UserDTO)
async def get_user(id: int):
    repo = UserHandler(repo=UserRepository())
    response = repo.get_user(id)
    return response


@router.post("/create-user", response_model=UserDTO)
async def create_user(dto: RegisterUserDTO):
    repo = UserHandler(repo=UserRepository())
    response = repo.add_user(dto)
    return response


@router.patch("/update-user", response_model=UserDTO)
async def update_user(dto: UpdateUserDTO):
    repo = UserHandler(repo=UserRepository())
    response = repo.update_user(dto)
    return response


@router.patch("/change-password")
async def change_password(dto: ChangePasswordDTO):
    repo = UserHandler(repo=UserRepository())
    try:
        repo.change_password(dto)
        return JSONResponse({"message": "Password changed."}, status_code=200)
    except ValueError as e:
        return JSONResponse({"message": str(e)}, status_code=200)
