from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from database.database import get_db
from crud import users

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post('/')
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return users.create_user(db, request)

