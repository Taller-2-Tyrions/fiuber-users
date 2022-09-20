from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..firebase_configs import get_pb
from ..schemas.users_schema import AuthBase

router = APIRouter(
    prefix="/login",
    tags=['Login']
)


@router.post('/')
async def login(request: AuthBase):
    try:
        user = get_pb().auth().sign_in_with_email_and_password(
                                        request.email, request.password)
        jwt = user['idToken']
        return JSONResponse(content={'token': jwt}, status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'There was an error logging in ' + str(err)},
                 status_code=400)
