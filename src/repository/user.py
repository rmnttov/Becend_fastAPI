from src.utils.repository import SQLAlchemyRepository
from src.model.user import UserModel
from sqlalchemy import select, or_
import logging

from src.scheme.users import UserFilter


class UserRepository(SQLAlchemyRepository):
    model = UserModel

    async def get_list(self, filter: UserFilter):
        async with self.async_session_maker() as session:
            stmt = select(UserModel)
            #if filter.user_uid is not None:
             #   stmt = stmt.where(UserModel.uid == filter.user_uid)
            if filter.search is not None:
                stmt = stmt.filter(
                    or_(
                        UserModel.name.ilike(f'%{filter.search}%'),
                        UserModel.email.ilike(f'%{filter.search}%'),
                    )
                )
            if filter.limit is not None:
                stmt = stmt.limit(filter.limit)
            if filter.offset is not None:
                stmt = stmt.offset(filter.offset)
            stmt = stmt.order_by('uid')

            query_result = await session.execute(stmt)
            logging.info(query_result)
            return query_result.scalars().all()
