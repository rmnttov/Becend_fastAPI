from fastapi.routing import APIRouter

from src.model.note import NoteModel
from src.scheme.users import User, UserFilter
from sqlalchemy import select, or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.users import User, UserFromDB
from src.model.user import UserModel

router = APIRouter()


class UserService:

    @staticmethod
    async def create_user(body: User, db_session: AsyncSession) -> UserFromDB:
        #logger.info(body)
        new_user = UserModel(name=body.name, email=body.email)
        db_session.add(new_user)
        await db_session.commit()
        return new_user


    @staticmethod
    async def get_users_list(filter_data: UserFilter, db_session: AsyncSession) -> list[UserModel]:
        if filter_data.user_uid is not None:
            stmt = (select(UserModel, NoteModel.title, NoteModel.text).where(UserModel.uid == filter_data.user_uid)
                    .join(NoteModel, UserModel.note_id == NoteModel.uid).group_by(
                UserModel.uid))  # на выходе один пользователь и его записки
        else:
            stmt = (select(UserModel, func.count(NoteModel.uid).label('notes_count'))
                    .join(NoteModel, UserModel.note_id == NoteModel.uid).group_by(UserModel.uid))# на выходе все пользователи + их количество записок
        if filter_data.search is not None:
            stmt = stmt.filter(
                or_(
                    UserModel.name.ilike(f'%{filter_data.search}%'),
                    UserModel.email.ilike(f'%{filter_data.search}%'),
                )
            )

        if filter_data.limit is not None and filter_data.limit > 0:
            stmt = stmt.limit(filter_data.limit)
        stmt = stmt.offset(filter_data.offset)
        stmt = stmt.order_by('uid')
        query_result = await db_session.execute(stmt)
        return query_result.scalars().all()

    @staticmethod
    async def update_user(body: User, uid: str, db_session: AsyncSession) -> UserFromDB:
        new_user_data = UserModel(**body.dict())
        db_session.filter_by(uid=uid).update(new_user_data)
        await db_session.commit()
        return new_user_data

    @staticmethod
    async def delete_user(uid: str, db_session: AsyncSession):
        db_session.filter_by(uid=uid).delete()
        await db_session.commit()
