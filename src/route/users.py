from fastapi.routing import APIRouter
from src.scheme.notes import Note

router = APIRouter()


users = []

@router.post('/')
def post_user(body: Note):
    users.append(body)


@router.get('/')
def get_users():
    return users


@router.patch('/{id}')
def update_user(body: Note, id: int):
    print(body.title)
    users[id] = body


@router.delete('/{id}')
def delete_user(id: int):
    users.pop(id)
