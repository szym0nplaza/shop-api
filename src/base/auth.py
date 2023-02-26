from fastapi import Cookie
from fastapi.security import SecurityScopes
from fastapi.exceptions import HTTPException
from config.settings import settings
from jose.exceptions import JWTError, ExpiredSignatureError
from modules.users.domain.models import User, Group
from config.settings import DBSession
from jose import jwt


def decode_email_from_token(token: str) -> str:
    """returns email or raises exception when expired or none"""
    if not token:
        raise JWTError
    return jwt.decode(token, key=settings.password_salt, algorithms="HS256").get(
        "email"
    )


def access_checker(
    allowed_roles: list,
    access_token: str,
):  
    session = DBSession().get_session()
    try:
        email = decode_email_from_token(access_token)
        user = session.query(User).filter_by(email=email).first()
        group = session.query(Group).filter_by(name=user.group).first()
        if not set([*allowed_roles, "__all__"]).intersection(set(group.perms.split(","))):
            raise HTTPException(detail="No permissions to access this view.", status_code=403)
    except (JWTError, ExpiredSignatureError) as e:
        raise HTTPException(detail=str(e), status_code=401)


def check_access(security_scopes: SecurityScopes, access_token: str = Cookie(None)):
    return access_checker(
        allowed_roles=security_scopes.scopes, access_token=access_token
    )
