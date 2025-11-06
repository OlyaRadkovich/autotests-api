from pydantic import BaseModel, Field, EmailStr


class UserSchemaV2(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchemaV2(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchemaV2(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchemaV2
