from fastapi import APIRouter, status
from ..schemas.users_schema import UserBase, DriverBase
from ..crud import crud
from ..database.mongo import db
from typing import Union


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get('/{user_id}')
def find_user(user_id: str):
    return crud.find_user(db, user_id)


@router.post('')
def create_user(user: Union[UserBase, DriverBase]):
    return crud.create_user(db, user)


@router.put('')
def update_user(user_id: str, changes: dict):
    return crud.update_user(db, user_id, changes)


@router.delete('/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_user(user_id: str):
    return crud.delete_user(db, user_id)
