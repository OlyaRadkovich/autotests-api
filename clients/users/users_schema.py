from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import get_random_email, get_random_password


class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=get_random_email)
    password: str = Field(default_factory=get_random_password)
    last_name: str = Field(alias="lastName", default="Lamarck")
    first_name: str = Field(alias="firstName", default="Jean-Baptiste")
    middle_name: str = Field(alias="middleName", default="de")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос об обновлении пользователя
    """
    user: UserSchema
