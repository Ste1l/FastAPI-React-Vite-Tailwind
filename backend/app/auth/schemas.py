import uuid
from fastapi_users import BaseUserManager, UUIDIDMixin
from app.models.models import User
from config import SECRET
from fastapi_users import schemas

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET