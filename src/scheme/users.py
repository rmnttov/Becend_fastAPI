from pydantic import BaseModel, Field


class User(BaseModel):
    name: str | None = Field(description="User name", default='Иванов')
    login: str | None = Field(description="User login", default='Ivanov')
    password: str | None = Field(description="User password", default='951753')