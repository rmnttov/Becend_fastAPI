from fastapi import Depends
from fastapi.routing import APIRouter
from pydantic import UUID4
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
async def post_user(body: User) -> UserFromDB:
    return await UserService.create_user(body)


@router.get('/{uid}')
async def get_user(uid: UUID4): #-> UserWithNotes:
    return await UserService.get_user(uid)

# f37588ea-bac0-46f8-a127-038b8e0d36aa

@router.post('/get-list/')
async def get_users(filter_data: UserFilter, db_session: AsyncSession = Depends(get_session)): #-> list[UserFromDB]:
    return await UserService.get_users_list(filter_data, db_session)


@router.patch('/{id}')
async def update_user(body: User, uid: str, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    return await UserService.update_user(body, db_session)


@router.delete('/{id}')
async def delete_user(uid: str, db_session: AsyncSession = Depends(get_session)) -> str:
    return await UserService.delete_user(uid, db_session)
    return 'слушаюсь и повинуюсь'
