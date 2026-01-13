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

