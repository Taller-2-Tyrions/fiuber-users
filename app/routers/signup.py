from fastapi import APIRouter
from firebase_admin import auth
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..schemas.users_schema import AuthBase


router = APIRouter(
    prefix="/signup",
    tags=['Sign Up']
)


@router.post('/')
async def signup(request: AuthBase):
    if request.email is None or request.password is None:
        raise HTTPException(detail={
                'message': 'Error! Missing Email or Password'},
                 status_code=400)
    try:
        user = auth.create_user(
            email=request.email,
            password=request.password
        )
        return JSONResponse(content={
                'message': f'Successfully created user {user.uid}'},
                     status_code=200)
    except Exception as err:
        raise HTTPException(detail={
            'message': 'Error Creating User '+str(err)}, status_code=400)
