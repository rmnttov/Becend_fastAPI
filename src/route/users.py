from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.users import User, UserFromDB
from src.model.user import UserModel
from src.adapter.db.session import get_session

router = APIRouter()

users = []

@router.post('/')
async def post_user(body: User, db_session: AsyncSession = Depends(get_session)) -> UserFromDB:
    # new_user = UserModel(**data.model_dump(exclude_unset=True))
    new_user = UserModel(name=body.name, email=body.email)
    db_session.add(new_user)
    await db_session.commit()
    return new_user
    # users.append(body)


@router.get('/')
async def get_users(age, db_session: AsyncSession = Depends(get_session)) -> list[UserFromDB]:
    # db_session.execute(f"SELECT * FROM users WHERE age >= {age}")
    # db_session.execute("SELECT * FROM users WHERE age >= :age", {'age': 21})
    query_result = await db_session.execute(select(UserModel))
    return query_result.scalars().all()


@router.patch('/{id}')
async def update_user(body: User, id: int):
    print(body.name)
    users[id] = body


@router.delete('/{id}')
async def delete_user(id: int):
    users.pop(id)
