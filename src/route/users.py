from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.users import User, UserFromDB, UserWithNotes, UserFilter
from src.scheme.notes import NoteFilter
from src.model.user import UserModel
from src.service.notes import NoteService
from src.adapter.db.session import get_session
from src.scheme.notes import NoteFromDB

import logging

from src.service.users import UserService

logger = logging.getLogger(__name__)

router = APIRouter()

users = []

# TODO move business logic to service

@router.post('/')
async def post_user(body: User, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    return await UserService.create_user(body, db_session)


@router.get('/{uid}')
async def get_user(filter_data: UserFilter, db_session: AsyncSession = Depends(get_session)): #-> UserWithNotes:
    #stmt = select(UserModel).filter(UserModel.uid == uid)
    #query_result = await db_session.execute(stmt)
    #user = query_result.scalars().first()
    # query_result = await db_session.execute(text(f"SELECT * FROM user WHERE uid = {uid}"))
    #notes_filter = NoteFilter(limit=0, offset=0, user_id=uid)
    #user_notes = [NoteFromDB(uid=n.uid, title=n.title, text=n.text, author_uid=n.author_uid) for n in await NoteService.get_notes_list(notes_filter, db_session)]
    #print(user_notes)
    #user_output = UserWithNotes(uid=user.uid, name=user.name, email=user.email, user_notes=user_notes)
    # user.user_notes = user_notes
    #return user_output
    return await UserService.get_users_list(filter_data, db_session)


@router.get('/')
async def get_users(filter_data: UserFilter, db_session: AsyncSession = Depends(get_session)): #-> list[UserFromDB]:
    return await UserService.get_users_list(filter_data, db_session)


@router.patch('/{id}')
async def update_user(body: User, uid: str, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    return await UserService.update_user(body, db_session)


@router.delete('/{id}')
async def delete_user(uid: str, db_session: AsyncSession = Depends(get_session)) -> str:
    return await UserService.delete_user(uid, db_session)
    return 'слушаюсь и повинуюсь'
