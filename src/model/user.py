import uuid
from sqlalchemy import UUID, Index, String
from sqlalchemy.orm import Mapped, mapped_column
from src.adapter.db.session import Base


class UserModel(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('email_indx', 'email'),
        # Index('date_created_user_uid_index', 'date_created', 'user_uid')
    )

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
