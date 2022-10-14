from fastapi import APIRouter, status
from ..schemas.users_schema import PassengerBase, DriverBase, Roles
from ..crud import crud
from ..database.mongo import db
from typing import Union
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get('/{user_id}/{user_caller}')
def find_user(user_id: str, user_caller: str):
    check_block_permissions(user_caller)
    found_user = crud.find_user(db, user_id)

    if not found_user:
        raise HTTPException(detail={
                'message': 'User Can\'t Be Found'},
                 status_code=404)

    if not has_full_access(user_id, user_caller):
        found_user = filter_accesible_content(found_user)

    return found_user


@router.post('')
def create_user(user: Union[PassengerBase, DriverBase]):
    check_already_created(user.id)
    roles = user.roles
    if has_admin_role(roles):
        raise HTTPException(detail={
                'message': 'Can\'t Create Admin User'},
                 status_code=404)

    return crud.create_user(db, user)


@router.put('/{user_id}/{user_caller}')
def update_user(user_id: str, changes: Union[PassengerBase, DriverBase],
                user_caller: str):
    changes.id = user_id
    check_block_permissions(user_caller)
    check_change_permissions(user_id, user_caller, "Update User")
    check_valid_change(changes, user_caller)
    return crud.update_user(db, user_id, changes)


@router.delete('/{user_id}/{user_caller}',
               status_code=status.HTTP_202_ACCEPTED)
def delete_user(user_id: str, user_caller: str):
    check_change_permissions(user_id, user_caller, "Delete User")
    return crud.delete_user(db, user_id)


def has_full_access(user_id, user_caller):
    return user_id == user_caller or isAdmin(user_caller)


def filter_accesible_content(found_user):
    found_user.pop("address", None)
    found_user.pop("roles")

    return found_user


def has_admin_role(roles):
    return Roles.ADMIN in roles


def isAdmin(id):
    user = crud.find_user(db, id)
    if user:
        roles = user.get("roles")
        return Roles.ADMIN in roles

    return False


def check_change_permissions(user_id, user_caller, action):
    if not has_full_access(user_id, user_caller):
        raise HTTPException(detail={
                'message': f'No Permissions To {action}'},
                 status_code=401)


def check_block_permissions(user_caller):
    if crud.is_blocked(db, user_caller):
        raise HTTPException(detail={
                'message': 'User Blocked'},
                 status_code=401)


def check_valid_change(changes, user_caller):
    roles = changes.roles

    has_admin = has_admin_role(roles)

    if not isAdmin(user_caller) and has_admin:
        raise HTTPException(detail={
                'message': 'No Permissions To Become Admin'},
                 status_code=401)


def check_already_created(user_id):
    if crud.is_registered(db, user_id):
        raise HTTPException(detail={
                'message': 'id Already Used'},
                 status_code=401)
