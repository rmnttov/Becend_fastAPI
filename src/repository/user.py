from src.utils.repository import SQLAlchemyRepository
from src.model.user import UserModel


class UserRepository(SQLAlchemyRepository):
    model = UserModel

    def get_list(self, **filter_by):
        pass
