from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Description of the file structure.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Description of the file creation request structure.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str = Field(default="./testdata/files/image.png")


class CreateFileResponseSchema(BaseModel):
    """
    Description of the file creation response structure.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Description of the file retrieval response structure.
    """
    file: FileSchema