from src.utils.repository import SQLAlchemyRepository
from src.model.note import NoteModel


class NoteRepository(SQLAlchemyRepository):
    model = NoteModel

    def get_list(self, **filter_by):
        pass
