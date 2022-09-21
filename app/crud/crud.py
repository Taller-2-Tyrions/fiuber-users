from fastapi.encoders import jsonable_encoder


def set_return_value(res):
    if res:
        return str(res)
    else:
        return None


def find_user(db, searched_id):
    return db["users"].find_one({"id": searched_id}, {"_id": 0})


def create_user(db, user):
    user_encoded = jsonable_encoder(user)
    value = db["users"].insert_one(user_encoded)
    return set_return_value(value)


def delete_user(db, user_id: str):
    user_found = db["users"].find_one_and_delete({"id": user_id})
    return set_return_value(user_found)


def update_user(db, user_id: str, changes: dict):
    user_found = db["users"].find_one_and_update({"id": user_id},
                                                 {"$set": changes})
    return set_return_value(user_found)
