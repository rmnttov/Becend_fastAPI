from pydantic import BaseModel, Field, UUID4


class Note(BaseModel):
    title: str | None = Field(description="Note title", default='Заголовк')
    text: str | None = Field(description="Note text", default=None)
    author_uid: UUID4 = Field(description="User uid")


class NoteFromDB(BaseModel):
    uid: UUID4 = Field(description="Note uid")
    title: str | None = Field(description="Note title", default='Заголовк')
    text: str | None = Field(description="Note text", default=None)
    author_uid: UUID4 = Field(description="User uid")


class NoteFilter(BaseModel):
    limit: int = Field(description="Note limit", default=10)
    offset: int = Field(description="Note offset", default=0)
    search: str | None = Field(description="Search text", default=None)
    author_uid: UUID4 | None = Field(description="Author uid", default=None)
