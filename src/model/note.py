import uuid
from sqlalchemy import UUID, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.adapter.db.session import Base


class NoteModel(Base):
    __tablename__ = 'note'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)

    author_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("user.uid"), nullable=False)

    user = relationship("User", backref="user_notes")
