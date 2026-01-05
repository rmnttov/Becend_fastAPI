from pydantic import BaseModel, Field


class Note(BaseModel):
    title: str | None = Field(description="Note title", default='Заголовк')
    text: str | None = Field(description="Note text", default=None)
    likes: int | None = Field(description="Number of kikes for current note", default=0, ge=0)

