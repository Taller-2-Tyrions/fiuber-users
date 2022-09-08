from fastapi import APIRouter
from ..schemas.usersSchema import UserBase
from ..crud import users
from ..database.mongo import db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post('/find_user')
def find_user(user: UserBase):
    return users.find_user(db, user.name)
