from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.users import User, UserFromDB, UserWithNotes
from src.scheme.notes import NoteFilter
from src.model.user import UserModel
from src.service.notes import NoteService
from src.adapter.db.session import get_session
from src.scheme.notes import NoteFromDB

import logging


logger = logging.getLogger(__name__)

router = APIRouter()

users = []

# TODO move business logic to service

@router.post('/')
async def post_user(body: User, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    # new_user = UserModel(**data.model_dump(exclude_unset=True))
    logger.info(body)
    new_user = UserModel(name=body.name, email=body.email)
    db_session.add(new_user)
    await db_session.commit()
    return new_user
    # users.append(body)


@router.get('/{uid}')
async def get_user(uid: str, db_session: AsyncSession = Depends(get_session)) -> UserWithNotes:
    stmt = select(UserModel).filter(UserModel.uid == uid)
    query_result = await db_session.execute(stmt)
    user = query_result.scalars().first()
    # query_result = await db_session.execute(text(f"SELECT * FROM user WHERE uid = {uid}"))
    notes_filter = NoteFilter(limit=0, offset=0, user_id=uid)
    user_notes = [NoteFromDB(uid=n.uid, title=n.title, text=n.text, author_uid=n.author_uid) for n in await NoteService.get_notes_list(notes_filter, db_session)]
    print(user_notes)
    user_output = UserWithNotes(uid=user.uid, name=user.name, email=user.email, user_notes=user_notes)
    # user.user_notes = user_notes
    return user_output


@router.get('/')
async def get_users(name_r, db_session: AsyncSession = Depends(get_session)) -> list[UserFromDB]:
    query_result = await db_session.execute(f"SELECT * FROM user WHERE name = {name_r}")
    # TODO use filter, limit, offset
    # db_session.execute("SELECT * FROM users WHERE age >= :age", {'age': 21})
    #logger.critical("critical message (on routes import)")
    #query_result = await db_session.execute(select(UserModel))
    return query_result.scalars().all()


@router.patch('/{id}')
async def update_user(body: User, uid: str, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    new_user_data = UserModel(name=body.name, email=body.email)
    db_session.filter_by(uid=uid).update(new_user_data)
    await db_session.commit()
    return new_user_data #Возвращается на фронт? da da


@router.delete('/{id}')
async def delete_user(uid: str, db_session: AsyncSession = Depends(get_session)) -> str:
    db_session.filter_by(uid=uid).delete()
    await db_session.commit()
    return 'слушаюсь и повинуюсь'
