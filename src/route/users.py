from fastapi.routing import APIRouter
from src.scheme.users import User

router = APIRouter()

users = []

@router.post('/')
def post_user(body: User):
    users.append(body)


@router.get('/')
def get_users():
    return users


@router.patch('/{id}')
def update_user(body: User, id: int):
    print(body.name)
    users[id] = body


@router.delete('/{id}')
def delete_user(id: int):
    users.pop(id)
