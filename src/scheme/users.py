from pydantic import BaseModel, Field, UUID4


class User(BaseModel):
    name: str | None = Field(description="User name", default='Иванов')
    email: str | None = Field(description="User email", default='ivanov@mail.com')
    password: str | None = Field(description="User password", default='951753')

class UserFromDB(BaseModel):
    uid: UUID4 = Field(description="User uid")
    name: str | None = Field(description="User name", default='Иванов')
    email: str | None = Field(description="User email", default='ivanov@mail.com')
