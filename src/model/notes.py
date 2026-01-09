import uuid
from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.adapter.db.session import Base


class Notes(Base):
    __tablename__ = 'notes'

    # id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    #author_id: ... #id автора