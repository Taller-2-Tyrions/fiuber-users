from fastapi import APIRouter
from ..schemas.profileimage import ImageBase
from ..firebase_configs import get_firebase, get_firebaseconfig
from firebase_admin import storage
from fastapi.exceptions import HTTPException

router = APIRouter(
    prefix="/users/{user_id}/profile/picture",
    tags=['profile picture']
)


def get_blob(user_id):
    bucket = storage.bucket(name=get_firebaseconfig()["storageBucket"],
                            app=get_firebase())

    blob = bucket.blob("profile-"+user_id)

    return blob


@router.post('')
def insert_image(user_id: str, img: ImageBase):
    get_blob(user_id).upload_from_string(
        img.img, content_type='application/octet-stream')

    return


@router.get('')
def retrieve_image(user_id: str):
    blob = get_blob(user_id)
    try:
        return {"img": blob.download_as_string()}
    except Exception:
        raise HTTPException(
                detail={'message': 'Image not found'},
                status_code=400)
