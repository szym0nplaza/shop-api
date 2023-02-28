from fastapi import APIRouter, Security
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from modules.users.infrastructure.repositories import UserRepository
from modules.users.infrastructure.auth import AuthModule
from modules.users.application.handlers import UserHandler, AuthHandler
from modules.users.infrastructure.ext import PaymentGateway
from modules.users.application.dto import (
    RegisterUserDTO,
    UserDTO,
    UpdateUserDTO,
    ChangePasswordDTO,
    LoginDTO,
    GroupDTO
)
from base.auth import check_access


users_router = router = APIRouter()


@router.post("/login")
async def login(dto: LoginDTO):
    auth_handler = AuthHandler(repo=UserRepository(), auth=AuthModule())
    auth_handler.check_password(dto)
    access_token, refresh_token = auth_handler.login(dto)
    response = JSONResponse({"message": "Successfully logged in."})
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
    return response


@router.get(
    "/users/{id}",
    response_model=UserDTO,
    dependencies=[Security(check_access, scopes=["view_user"])],
)
async def get_user(id: int):
    handler = UserHandler(repo=UserRepository(), payments=PaymentGateway())
    response = handler.get_user(id)
    return response


@router.get(
    "/groups",
    dependencies=[Security(check_access, scopes=["view_group"])],
)
async def get_groups():
    handler = AuthHandler(repo=UserRepository(), auth=AuthModule())
    response = handler.get_groups()
    return response

@router.get(
    "/perms-list",
    dependencies=[Security(check_access, scopes=["view_group"])],
)
async def get_perms_list():
    handler = AuthHandler(repo=UserRepository(), auth=AuthModule())
    response = handler.get_perms()
    return response

@router.patch(
    "/groups/{name}",
    dependencies=[Security(check_access, scopes=["manage_group"])],
)
async def update_group(dto: GroupDTO):
    handler = AuthHandler(repo=UserRepository(), auth=AuthModule())
    response = handler.modify_group(dto)
    return response


@router.post("/create-user", response_model=UserDTO)
async def create_user(dto: RegisterUserDTO):
    handler = UserHandler(repo=UserRepository(), payments=PaymentGateway())
    # try:
    response = handler.add_user(dto)
    # except IntegrityError:
    #     raise HTTPException(detail="Provided group name not found.", status_code=404)
    return response


@router.patch(
    "/update-user",
    response_model=UserDTO,
    dependencies=[Security(check_access, scopes=["manage_user"])],
)
async def update_user(dto: UpdateUserDTO):
    handler = UserHandler(repo=UserRepository(), payments=PaymentGateway())
    response = handler.update_user(dto)
    return response


@router.patch(
    "/change-password", dependencies=[Security(check_access, scopes=["manage_user"])]
)
async def change_password(dto: ChangePasswordDTO):
    handler = UserHandler(repo=UserRepository(), payments=PaymentGateway())
    try:
        handler.change_password(dto)
        return JSONResponse({"message": "Password changed."}, status_code=200)
    except ValueError as e:
        return JSONResponse({"message": str(e)}, status_code=200)
