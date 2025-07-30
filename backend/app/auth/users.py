import uuid
from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import User
from app.auth.schemas import UserCreate, UserManager, UserRead
from db import get_async_session
from config import SECRET

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

jwt_authentication = JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=lambda: jwt_authentication,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
users_router = fastapi_users.get_users_router(UserRead, UserCreate)