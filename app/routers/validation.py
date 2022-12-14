from fastapi import APIRouter
from firebase_admin import auth
from ..schemas.users_schema import TokenBase
from fastapi.exceptions import HTTPException
from ..crud import crud
from ..database.mongo import db

router = APIRouter(
    prefix="/validate",
    tags=['Validate']
)


@router.post('/')
async def validate(request: TokenBase):
    try:
        jwt = request.token
        user = auth.verify_id_token(jwt)
        uid = user["uid"]
        roles = crud.get_roles(db, uid)
        blocked = crud.is_blocked(db, uid)
        return {"uid": uid, "roles": roles, "is_blocked": blocked}
    except Exception as err:
        raise HTTPException(detail={
            'message': 'Error validating token: '+str(err)}, status_code=400)
