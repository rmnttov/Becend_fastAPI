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
        return await user_repository.get_list()
        # TODO список пользователей
        #stmt = select(UserModel)
        #if filter_data.user_uid is not None:
         #   stmt = stmt.where(UserModel.uid == filter_data.user_uid)
        #if filter_data.search is not None:
         #   stmt = stmt.filter(
          #      or_(
           #         UserModel.name.ilike(f'%{filter_data.search}%'),
            #        UserModel.email.ilike(f'%{filter_data.search}%'),
             #   )
            #)
        #if filter_data.limit is not None and filter_data.limit > 0:
         #   stmt = stmt.limit(filter_data.limit)
        #stmt = stmt.offset(filter_data.offset)
 #       stmt = stmt.order_by('uid')

        # TODO add notes (a zahem?)
 #       query_result = await db_session.execute(stmt)
  #      return query_result.scalars().all()

    @staticmethod
    async def update_user(body: User, uid) -> UserFromDB:
        return await user_repository.update_one(body.dict(), uid)
        # TODO todo todo
        #new_user_data = UserModel(**body.dict())
        #db_session.filter_by(uid=uid).update(new_user_data)
        #await db_session.commit()
        #return new_user_data

    @staticmethod
    async def delete_user(uid: UUID4):
        return await user_repository.delete_one(uid)
        #db_session.filter_by(uid=uid).delete()
        #await db_session.commit()

#706df4d6-130f-4ca3-92c3-92eeafaa48f0
#815a6554-106d-43b5-b6fe-6b934bc6c46e