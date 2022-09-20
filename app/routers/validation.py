from fastapi import APIRouter
from firebase_admin import auth
from ..schemas.users_schema import TokenBase

router = APIRouter(
    prefix="/validate",
    tags=['Validate']
)


@router.post('/')
async def validate(request: TokenBase):
    jwt = request.token
    user = auth.verify_id_token(jwt)
    return user["uid"]
