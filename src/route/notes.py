from fastapi.routing import APIRouter
from src.scheme.notes import Note, NoteFilter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.notes import Note, NoteFromDB
from src.service.notes import NoteService
from src.adapter.db.session import get_session

router = APIRouter()


@router.post('/')
async def post_notes(body: Note) -> NoteFromDB:
    return await NoteService.create_note(body)


@router.post('/list/')
async def get_notes(filter_data: NoteFilter, db_session: AsyncSession = Depends(get_session)) -> list[NoteFromDB]:
    return await NoteService.get_notes_list(filter_data, db_session)


@router.patch('/{id}')
async def update_note(body: Note, uid: str) -> NoteFromDB:
    return await NoteService.update_note(body, uid)


@router.delete('/{id}')
async def delete_note(uid: str) -> None:
    return await NoteService.delete_note(uid)
