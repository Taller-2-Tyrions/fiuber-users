from app.schemas.usersSchema import UserBase

def set_return_value(res):
    if res:
        return str(res)
    else:
        return None

def find_user(db, searched_id):
    user_found = db["users"].find_one({"id":searched_id}, {"_id":0})
    if user_found:
       return user_found
    return db["drivers"].find_one({"id":searched_id}, {"_id":0})

def create_user(db, user):
    if isinstance(user,UserBase):
        value = db["users"].insert_one(vars(user))
    else:
        value = db["drivers"].insert_one(vars(user))

    return set_return_value(value)

def delete_user(db, user_id: str):
    user_found = db["users"].find_one_and_delete({"id":user_id})
    if user_found:
        return set_return_value(user_found)
    driver_found = db["drivers"].find_one_and_delete({"id":user_id})
    return set_return_value(driver_found)

def update_user(db, user_id: str, changes:dict):
    user_found = db["users"].fin_one_and_update({"id":user_id}, {"$set":changes})
    if user_found:
        return set_return_value(user_found)
    driver_found = db["drivers"].fin_one_and_update({"id":user_id}, {"$set":changes})
    return set_return_value(driver_found)