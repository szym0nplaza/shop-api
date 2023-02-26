from modules.users.application.handlers import UserHandler, AuthHandler
from modules.users.application.dto import (
    RegisterUserDTO,
    UserDTO,
    UpdateUserDTO,
    ChangePasswordDTO,
    LoginDTO,
)
from .conftest import MockUserRepo, MockAuthModule
from copy import deepcopy
from typing import Dict, Any


class TestUserHandler:
    _user_handler = UserHandler(repo=MockUserRepo())
    _auth_handler = AuthHandler(repo=MockUserRepo(), auth=MockAuthModule())
    _data_dict: Dict[str, Any] = {
        "email": "test@testmail.com",
        "name": "Test",
        "surname": "TestSur",
        "group": "admin",
        "password": "zaq1@WSX",
    }

    def test_user_creation(self):
        data_dict = deepcopy(
            self._data_dict
        )  # Copy dict to prevent changes in base variable
        dto = RegisterUserDTO(**data_dict)
        result = self._user_handler.add_user(dto)

        data_dict["id"] = 1
        data_dict.pop("password")

        assert result.__dict__ == data_dict

    def test_user_get(self):
        data_dict = deepcopy(self._data_dict)
        data_dict["id"] = 1
        data_dict.pop("password")

        result = self._user_handler.get_user(1)

        assert isinstance(result, UserDTO)
        assert result.__dict__ == data_dict

    def test_user_update(self):
        _update_data_dict: Dict[str, Any] = {
            "id": 1,
            "email": "test2@testmail.com",
            "name": "TestTest",
            "surname": "TestSurname123",
            "group": "customer",
        }
        update_data = UpdateUserDTO(**_update_data_dict)

        self._user_handler.update_user(update_data)
        updated_user = self._user_handler.get_user(1)

        assert _update_data_dict == updated_user.__dict__

    def test_password_change(self):
        _update_pass_data = {"id": 1, "new_password": "n3WP@ssword"}
        dto = ChangePasswordDTO(**_update_pass_data)

        self._user_handler.change_password(dto)
        dto = LoginDTO(email="test2@testmail.com", given_password="n3WP@ssword")

        assert self._auth_handler.check_password(dto)
