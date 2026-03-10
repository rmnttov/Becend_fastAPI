from fastapi.routing import APIRouter
from src.scheme.notes import Note, NoteFilter, NoteUpdate
from pydantic import UUID4
from src.scheme.notes import Note, NoteFromDB
from src.service.notes import NoteService

router = APIRouter()


@router.post('/')
async def post_notes(body: Note) -> NoteFromDB:
    return await NoteService.create_note(body)


@router.post('/list/')
async def get_notes(filter_data: NoteFilter) -> list[NoteFromDB]:
    return await NoteService.get_notes_list(filter_data)


@router.patch('/{uid}')
async def update_note(body: NoteUpdate, uid: UUID4):# -> NoteFromDB:
    return await NoteService.update_note(body, uid)


@router.delete('/{uid}')
async def delete_note(uid: UUID4) -> None:
    return await NoteService.delete_note(uid)

@router.post('/summarize/{input_note_uid}')
async def generate_note(input_note_uid: UUID4) -> NoteFromDB:
    return await NoteService.generate_note(input_note_uid)
