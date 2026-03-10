from src.scheme.notes import NoteFilter
from src.utils.repository import SQLAlchemyRepository
from sqlalchemy import select, or_
from src.model.note import NoteModel


class NoteRepository(SQLAlchemyRepository):
    model = NoteModel

    async def get_list(self, filter: NoteFilter):
        async with self.async_session_maker() as session:
            stmt = select(NoteModel)
            if filter.author_uid is not None:
                stmt = stmt.where(NoteModel.author_uid == filter.author_uid)
            if filter.search is not None:
                stmt = stmt.filter(
                    or_(
                        NoteModel.title.ilike(f'%{filter.search}%'),
                        NoteModel.text.ilike(f'%{filter.search}%'),
                    )
                )
            if filter.limit is not None:
                stmt = stmt.limit(filter.limit)
            if filter.offset is not None:
                stmt = stmt.offset(filter.offset)
            stmt = stmt.order_by('uid')

            query_result = await session.execute(stmt)
            return query_result.scalars().all()
