from src.utils.repository import SQLAlchemyRepository
from src.model.user import UserModel
from sqlalchemy import select, or_

from src.scheme.users import UserFilter


class UserRepository(SQLAlchemyRepository):
    model = UserModel

    async def get_list(self, filter: UserFilter):
        async with self.async_session_maker() as session:
            stmt = select(UserModel)
            if filter.user_uid is not None:
                stmt = stmt.where(UserModel.uid == filter.user_uid)
            if filter.search is not None:
                stmt = stmt.filter(
                    or_(
                        UserModel.name.ilike(f'%{filter.search}%'),
                        UserModel.email.ilike(f'%{filter.search}%'),
                    )
                )
            if filter.limit is not None and filter.limit > 0:
                stmt = stmt.limit(filter.limit)
                stmt = stmt.offset(filter.offset)
                stmt = stmt.order_by('uid')

            query_result = session.execute(stmt)
            return query_result.scalars().all()
