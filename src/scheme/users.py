from pydantic import BaseModel, Field, UUID4

from src.scheme.notes import NoteFromDB


class User(BaseModel):
    name: str | None = Field(description="User name", default='Иванов')
    email: str | None = Field(description="User email", default='ivanov@mail.com')
    password: str | None = Field(description="User password", default='951753')


class UserFromDB(BaseModel):
    uid: UUID4 = Field(description="User uid")
    name: str | None = Field(description="User name", default='Иванов')
    email: str | None = Field(description="User email", default='ivanov@mail.com')


class UserWithNotes(BaseModel):
    uid: UUID4 = Field(description="User uid")
    name: str | None = Field(description="User name", default='Иванов')
    email: str | None = Field(description="User email", default='ivanov@mail.com')
    user_notes: list[NoteFromDB] | None = Field(description="User notes", default=None)

class UserFilter(BaseModel):
    limit: int = Field(description="Note limit", default=10)
    offset: int = Field(description="Note offset", default=0)
    search: str | None = Field(description="Search text", default=None)
    user_uid: UUID4 | None = Field(description="User uid", default=None)
