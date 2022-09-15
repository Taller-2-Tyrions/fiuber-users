from fastapi import APIRouter, Request
from firebase_admin import auth
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..schemas.usersSchema import TokenBase

router = APIRouter(
    prefix="/validate",
    tags=['Validate']
)

@router.post('/')
async def validate(request: TokenBase):
   jwt = request.token
   user = auth.verify_id_token(jwt)
   return user["uid"]
