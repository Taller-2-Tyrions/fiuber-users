from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..firebase_configs import get_pb
from firebase_admin import auth
from ..schemas.users_schema import AuthBase, TokenBase
from ..database.mongo import db
from ..crud import crud
from .users import check_block_permissions

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
        missing_register = crud.is_registered(db, user["localId"])
        check_block_permissions(user["localId"])
        return JSONResponse(content={'token': jwt,
                                     'is_registered': missing_register},
                            status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'There was an error logging in ' + str(err)},
                 status_code=400)


@router.get('/password-recovery', status_code=status.HTTP_200_OK)
async def send_recover_email(email: str):
    try:
        get_pb().auth().send_password_reset_email(email)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'There was an error sending recovery mail' + str(err)},
                 status_code=400)


@router.post('/google')
async def login_google(request: TokenBase):
    try:
        jwt = request.token
        user = auth.verify_id_token(jwt)
        missing_register = crud.is_registered(db, user["localId"])
        check_block_permissions(user["localId"])
        return JSONResponse(content={'token': jwt,
                                     'is_registered': missing_register},
                            status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'Error validating token: '+str(err)}, status_code=400)
