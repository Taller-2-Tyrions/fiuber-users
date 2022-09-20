import mongomock
from app.schemas import users_schema
from app.crud import crud


def test_create_user():
    db = mongomock.MongoClient().db
    user_id = "10"
    name_asked = "Santix"
    user_example = users_schema.UserBase(id=user_id, name=name_asked,
                                         last_name="F", address="faraway")
    crud.create_user(db, user_example)

    user_found = crud.find_user(db, user_id)

    assert (user_found.get("name") == name_asked)


def test_create_driver():
    db = mongomock.MongoClient().db
    driver_id = "100a"
    name_asked = "Nachox"
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", car="reno12")
    crud.create_user(db, driver_example)

    driver_found = crud.find_user(db, driver_id)

    assert (driver_found.get("name") == name_asked)


def test_update_driver():
    db = mongomock.MongoClient().db
    driver_id = "100a"
    name = "Nachox"

    driver_example = users_schema.DriverBase(id=driver_id, name=name,
                                             last_name="F", car="reno12")
    crud.create_user(db, driver_example)

    new_name = "Santix"
    changes = {"name": new_name}

    crud.update_user(db, driver_id, changes=changes)
    driver_found = crud.find_user(db, driver_id)

    assert (driver_found.get("name") == new_name)


def test_multiple_update_driver():
    db = mongomock.MongoClient().db
    driver_id = "100a"
    name = "Nachox"
    last_name = "F"
    driver_example = users_schema.DriverBase(id=driver_id, name=name,
                                             last_name=last_name, car="reno12")
    crud.create_user(db, driver_example)

    new_name = "Santix"
    new_car = "lambo"

    changes = {"name": new_name, "car": new_car}
    crud.update_user(db, driver_id, changes=changes)
    driver_found = crud.find_user(db, driver_id)

    assert (driver_found.get("name") == new_name)
    assert (driver_found.get("car") == new_car)
    assert (driver_found.get("last_name") == last_name)


def test_delete_user():
    db = mongomock.MongoClient().db
    user_id = "10"
    name_asked = "Santix"
    user_example = users_schema.UserBase(id=user_id, name=name_asked,
                                         last_name="F", address="faraway")
    crud.create_user(db, user_example)

    user_found = crud.find_user(db, user_id)

    assert (user_found.get("name") == name_asked)

    crud.delete_user(db, user_id=user_id)

    user_found = crud.find_user(db, user_id)

    assert (user_found is None)
