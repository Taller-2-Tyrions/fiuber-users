from pydantic import BaseModel
from typing import List
from enum import Enum


class Roles(Enum):
    PASSENGER = "Passenger"
    DRIVER = "Driver"
    ADMIN = "Admin"


class CarBase(BaseModel):
    model: str
    year: int
    plaque: str
    capacity: int


class PersonBase(BaseModel):
    id: str
    name: str
    last_name: str
    roles: List[Roles]
    is_blocked: bool


class PassengerBase(PersonBase):
    address: str


class DriverBase(PersonBase):
    car: CarBase


class AuthBase(BaseModel):
    email: str
    password: str


class TokenBase(BaseModel):
    token: str


class RecoveryEmailBase(BaseModel):
    email: str
