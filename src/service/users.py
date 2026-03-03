from fastapi.routing import APIRouter
from pydantic import UUID4

from src.model.note import NoteModel
from src.scheme.users import User, UserFilter
from sqlalchemy import select, or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.users import User, UserFromDB
from src.model.user import UserModel
from src.repository.user import UserRepository

router = APIRouter()

user_repository = UserRepository()

class UserService:

    @staticmethod
    async def create_user(body: User) -> UserModel:
        return await user_repository.add_one(body.dict())

    @staticmethod
    async def get_user(uid: UUID4) -> UserModel:
        return await user_repository.get_one(uid=str(uid))

    @staticmethod
    async def get_users_list(filter_data: UserFilter) -> list[UserModel]:
        return await user_repository.get_list(filter_data)

    @staticmethod
    async def update_user(body: User, uid): #-> UserFromDB:
        return await user_repository.update_one(body.dict(), uid)

    @staticmethod
    async def delete_user(uid: UUID4):
        return await user_repository.delete_one(uid)
