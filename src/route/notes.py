from fastapi.routing import APIRouter
from src.scheme.notes import Note

router = APIRouter()

notes = []


@router.post('/')
def post_notes(body: Note):
    notes.append(body)

@router.get('/')
def get_notes():
    return notes


@router.patch('/{id}')
def update_note(body: Note, id: int):
    print(body.title)
    notes[id] = body



@router.delete('/{id}')
def delete_note(id: int):
    notes.pop(id)  # id верный берётся?

# @router.get("/")
# def hi_mam():
#     return "hi"
#
#
# @router.get("/calc/{a}/{b}")
# def hi_mam(a: int, b: int):
#     return a + b
#
#
# @router.post("/some-post")
# def hi_mam(body: dict):
#     return body['param']

