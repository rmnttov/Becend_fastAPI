from abc import ABC, abstractmethod

from sqlalchemy import select, or_, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.db.session import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    # @abstractmethod
    # async def update_one():
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def delete_one():
    #     raise NotImplementedError

    @abstractmethod
    async def get_list():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self):
        self.async_session_maker = async_session_maker

    async def add_one(self, data: dict):
        obj = self.model(**data)
        async with self.async_session_maker() as session:
            session.add(obj)
            await session.commit()
        return obj

    async def get_one(self, **filter_by):
        async with self.async_session_maker() as session:
            query = select(self.model).filter_by(**filter_by)
            res = await session.execute(query)
            res = res.scalar_one_or_none()
        return res

    async def update_one(self, data: dict, uid):
        if not uid:
            raise ValueError("uid is required for update")

        async with self.async_session_maker() as session:
            query = update(self.model).where(self.model.uid == uid).values(**data)

            await session.execute(query)
            await session.commit()

        return "Обновляем"

    async def delete_one(self, uid):
        async with self.async_session_maker() as session:
            stmt = delete(self.model).where(self.model.uid == uid)

            await session.execute(stmt)
            await session.commit()

        return "Удаляем"

    async def get_list(self):
        async with self.async_session_maker() as session:
            query = select(self.model)
            res = await session.execute(query)
            # res = [row.serialize() for row in res.all()]
        return res
