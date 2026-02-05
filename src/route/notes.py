from fastapi.routing import APIRouter
from src.scheme.notes import Note
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.notes import Note, NoteFromDB
from src.model.note import NoteModel
from src.adapter.db.session import get_session

router = APIRouter()

notes = []


@router.post('/')
async def post_notes(body: Note, db_session: AsyncSession = Depends(get_session)) -> NoteFromDB:
    # notes.append(body)
    new_note = NoteModel(title=body.title, text=body.text)
    db_session.add(new_note)
    await db_session.commit()
    return new_note



@router.get('/')
async def get_notes(len_r, db_session: AsyncSession = Depends(get_session))-> list[NoteFromDB]:
    query_result = await db_session.execute(f"SELECT * FROM note WHERE CHAR_LENGTH(text) >= {len_r}") #получение записок где длинна больше или равна len_r
    #query_result = await db_session.execute(select(NoteModel))
    return query_result.scalars().all()
#return notes


@router.patch('/{id}')
async def update_note(body: Note, id: int, db_session: AsyncSession = Depends(get_session)) -> NoteFromDB:
    new_note_data = NoteModel(title=body.title, text=body.text)
    db_session.filter_by(uid=id).update(new_note_data)
    await db_session.commit()
    #print(body.title)
    #notes[id] = body
    return new_note_data #Возвращается на фронт?



@router.delete('/{id}')
async def delete_note(id: int, db_session: AsyncSession = Depends(get_session)) -> None:
    db_session.filter_by(uid=id).delete()
    await db_session.commit()

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
