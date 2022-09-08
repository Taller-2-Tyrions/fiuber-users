
def find_user(db, user_name):
    return db["users"].find_one({"name":user_name},{'_id': 0})