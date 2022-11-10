from fastapi.encoders import jsonable_encoder
from pymongo import ReturnDocument


def set_return_value(res):
    if res:
        return str(res)
    else:
        return None


def find_user(db, searched_id) -> dict:
    return db["users"].find_one({"id": searched_id}, {"_id": 0})


def find_all_users(db) -> dict:
    return db["users"].find({})


def create_user(db, user):
    user_encoded = jsonable_encoder(user)
    value = db["users"].insert_one(user_encoded)
    return set_return_value(value)


def delete_user(db, user_id: str):
    user_found = db["users"].find_one_and_delete({"id": user_id})
    return set_return_value(user_found)


def update_user(db, user_id: str, changes):
    changes = jsonable_encoder(changes)
    roles = changes.get("roles")
    after = ReturnDocument.AFTER

    if roles:
        actual_roles = find_user(db, user_id).get("roles")
        actual_roles.extend(x for x in roles if x not in actual_roles)
        changes.update({"roles": actual_roles})

    user_found = db["users"].find_one_and_update({"id": user_id},
                                                 {"$set": changes},
                                                 return_document=after)
    return set_return_value(user_found)


def is_registered(db, user_id: str):
    return db["users"].count_documents({"id": user_id}, limit=1) > 0


def get_roles(db, user_id: str):
    if (not is_registered(db, user_id)):
        return []
    return find_user(db, user_id).get("roles")


def is_blocked(db, user_id):
    if (not is_registered(db, user_id)):
        return False
    return find_user(db, user_id).get("is_blocked")
