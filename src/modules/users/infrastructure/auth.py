from modules.users.application.intefraces import IAuthModule
from jose import jwt
from datetime import datetime, timedelta
from config.settings import settings
from typing import Tuple


class AuthModule(IAuthModule):
    def create_tokens(self, email: str) -> Tuple[str, str]:
        token_expire = datetime.utcnow()
        data = {"email": email}

        access_token = jwt.encode(
            claims={
                "exp": token_expire + timedelta(minutes=60),
                **data,
            },
            key=settings.password_salt,
            algorithm="HS256",
        )

        refresh_token = jwt.encode(
            claims={
                "exp": token_expire + timedelta(days=7),
                **data,
            },
            key=settings.password_salt,
            algorithm="HS256",
        )
        return access_token, refresh_token
