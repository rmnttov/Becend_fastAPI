import asyncio
from fastapi.routing import APIRouter

from src.repository.note import NoteRepository
from src.scheme.notes import Note, NoteFilter, NoteUpdate
from src.scheme.notes import Note, NoteFromDB
from src.model.note import NoteModel

from src.adapter.ollama.llm_calls import call_ollama

router = APIRouter()

note_repository = NoteRepository()


class NoteService:

    @staticmethod
    async def create_note(body: Note) -> NoteFromDB:
        return await note_repository.add_one(body.dict())

    @staticmethod
    async def get_notes_list(filter_data: NoteFilter) -> list[NoteModel]:
        return await note_repository.get_list(filter_data)

    @staticmethod
    async def update_note(body: NoteUpdate, uid: str) -> NoteFromDB:
        return await note_repository.update_one(body.dict(), uid)


    @staticmethod
    async def delete_note(uid: str):
        return await note_repository.delete_one(uid)

    @staticmethod
    async def generate_note_with_ai(uid: str, input_note: Note):
        print(123)
        ollama_response = call_ollama(input_note.title, input_note.text)
        await note_repository.update_one(
            {
                'uid': uid,
                'text': ollama_response
            },
            uid
        )

    @staticmethod
    async def generate_note(input_note_uid: str) -> Note:
        input_note = await note_repository.get_one(uid=input_note_uid)
        result_note = await note_repository.add_one({
            'title': f'{input_note.title} RETELLING',
            'text': 'handling ...',
            'author_uid': input_note.author_uid,
        })
        print(123)
        asyncio.create_task(
            NoteService.generate_note_with_ai(result_note.uid, input_note)
        )
        return result_note
