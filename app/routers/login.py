from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..firebase_configs import get_pb
from firebase_admin import db as firebase_db
from firebase_admin import auth
from ..schemas.users_schema import GoogleLoginBase, RecoveryEmailBase
from ..schemas.users_schema import LoginAuthBase
from ..database.mongo import db
from ..crud import crud
from .users import check_block_permissions


router = APIRouter(
    prefix="/login",
    tags=['Login']
)


def push_token(device_token, user_id):
    ref = firebase_db.reference("/"+user_id)
    push_data = {"token": device_token}
    ref.set(push_data)


@router.post('/')
async def login(request: LoginAuthBase):
    try:
        user = get_pb().auth().sign_in_with_email_and_password(
                                        request.email, request.password)
        jwt = user['idToken']
        user_id = user["localId"]
        missing_register = crud.is_registered(db, user_id)
        check_block_permissions(user_id)
        push_token(request.device_token, user_id)
        return JSONResponse(content={'token': jwt,
                                     'is_registered': missing_register,
                                     'id': user["localId"]},
                            status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'There was an error logging in ' + str(err)},
                 status_code=400)


@router.post('/password-recovery', status_code=status.HTTP_200_OK)
async def send_recover_email(email: RecoveryEmailBase):
    try:
        get_pb().auth().send_password_reset_email(email.email)
    except Exception as err:
        raise HTTPException(detail={'message':
              'There was an error sending recovery mail. ' + str(err)},
                            status_code=400)


@router.post('/google')
async def login_google(request: GoogleLoginBase):
    try:
        jwt = request.token
        user = auth.verify_id_token(jwt)
        user_id = user["user_id"]
        missing_register = crud.is_registered(db, user_id)
        check_block_permissions(user_id)
        push_token(request.device_token, user_id)
        return JSONResponse(content={'token': jwt,
                                     'is_registered': missing_register,
                                     'id': user_id},
                            status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'Error validating token: '+str(err)}, status_code=400)
