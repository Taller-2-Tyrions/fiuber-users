from pydantic import BaseModel


class ImageBase(BaseModel):
    img: str
