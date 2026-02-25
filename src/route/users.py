from fastapi.routing import APIRouter
from pydantic import UUID4
from src.scheme.users import User, UserFromDB, UserWithNotes, UserFilter

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
async def get_users(filter_data: UserFilter): #-> list[UserFromDB]:
    return await UserService.get_users_list(filter_data)


@router.patch('/{uid}')
async def update_user(body: User, uid: UUID4) -> UserFromDB:
    return await UserService.update_user(body, uid)


@router.delete('/{uid}')
async def delete_user(uid: UUID4) -> str:
    return await UserService.delete_user(uid)
