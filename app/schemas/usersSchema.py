from pydantic import BaseModel


class PersonBase(BaseModel):
    id: str
    name: str
    last_name: str

class UserBase(PersonBase):
    address: str

class DriverBase(PersonBase):
    car: str