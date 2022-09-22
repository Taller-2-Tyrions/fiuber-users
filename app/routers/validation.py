from fastapi import APIRouter
from firebase_admin import auth
from ..schemas.users_schema import TokenBase
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix="/validate",
    tags=['Validate']
)


@router.post('/')
async def validate(request: TokenBase):
    try:
        jwt = request.token
        user = auth.verify_id_token(jwt)
        return {"uid": user["uid"]}
    except Exception as err:
        raise HTTPException(detail={
            'message': 'Error validating token: '+str(err)}, status_code=400)
