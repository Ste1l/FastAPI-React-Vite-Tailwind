from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin, ModelView
from app.auth.users import auth_router, register_router, users_router
from app.models.models import User
from db import engine

app = FastAPI()

#admin-panel
admin = Admin(app, engine)

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.is_active, User.is_superuser, User.is_verified]

admin.add_view(UserAdmin)
#End admin-panel

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, prefix="/auth/jwt", tags=["auth"])
app.include_router(register_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
