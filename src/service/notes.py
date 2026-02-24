from fastapi.routing import APIRouter

from src.repository.note import NoteRepository
from src.scheme.notes import Note, NoteFilter
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from src.scheme.notes import Note, NoteFromDB
from src.model.note import NoteModel

router = APIRouter()

note_repository = NoteRepository()


class NoteService:

    @staticmethod
    async def create_note(body: Note) -> NoteFromDB:
        return await note_repository.add_one(body.dict())
        #new_note = NoteModel(**body.dict())
        #db_session.add(new_note)
        #await db_session.commit()
        #return new_note

    @staticmethod
    async def get_notes_list(filter_data: NoteFilter, db_session: AsyncSession) -> list[NoteModel]:
        stmt = select(NoteModel)
        if filter_data.search is not None:
            stmt = stmt.filter(
                or_(
                    NoteModel.title.ilike(f'%{filter_data.search}%'),
                    NoteModel.text.ilike(f'%{filter_data.search}%'),
                )
            )
        if filter_data.user_uid is not None:
            stmt = stmt.filter(NoteModel.author_uid == filter_data.user_uid)
        if filter_data.limit is not None and filter_data.limit > 0:
            stmt = stmt.limit(filter_data.limit)
        stmt = stmt.offset(filter_data.offset)
        stmt = stmt.order_by('uid')
        query_result = await db_session.execute(stmt)
        return query_result.scalars().all()

    @staticmethod
    async def update_note(body: Note, uid: str) -> NoteFromDB:
        return await note_repository.update_one(body.dict(), uid)
        #new_note_data = NoteModel(**body.dict())
        #db_session.filter_by(uid=uid).update(new_note_data)
        #await db_session.commit()
        #return new_note_data

    @staticmethod
    async def delete_note(uid: str):
        return await note_repository.delete_one(uid)
        #db_session.filter_by(uid=uid).delete()
        #await db_session.commit()
