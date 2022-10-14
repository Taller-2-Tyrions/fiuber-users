import mongomock
from app.schemas import users_schema
from app.crud import crud
from app.schemas.users_schema import PassengerBase


def test_create_user():
    db = mongomock.MongoClient().db
    user_id = "10"
    name_asked = "Santix"
    user_example = PassengerBase(id=user_id, name=name_asked,
                                 last_name="F", roles=["Passenger"],
                                 address="faraway", is_blocked=False)
    crud.create_user(db, user_example)

    user_found = crud.find_user(db, user_id)

    assert (user_found.get("name") == name_asked)


def test_create_driver():
    db = mongomock.MongoClient().db
    driver_id = "100a"
    name_asked = "Nachox"
    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", roles=["Driver"],
                                             car=car_example, is_blocked=False)
    crud.create_user(db, driver_example)

    driver_found = crud.find_user(db, driver_id)

    assert (driver_found.get("name") == name_asked)


def test_update_driver():
    db = mongomock.MongoClient().db
    driver_id = "100a"
    name = "Nachox"

    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name,
                                             last_name="F",
                                             roles=["Passenger"],
                                             car=car_example, is_blocked=False)
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
    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name,
                                             last_name="F",
                                             roles=["Passenger"],
                                             car=car_example, is_blocked=False)
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
    driver_id = "10"
    name_asked = "Santix"

    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", roles=["Driver"],
                                             car=car_example, is_blocked=False)
    crud.create_user(db, driver_example)

    user_found = crud.find_user(db, driver_id)

    assert (user_found.get("name") == name_asked)

    crud.delete_user(db, user_id=driver_id)

    user_found = crud.find_user(db, driver_id)

    assert (user_found is None)


def test_user_in_db():
    db = mongomock.MongoClient().db
    driver_id = "10"
    name_asked = "Santix"

    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", roles=["Driver"],
                                             car=car_example, is_blocked=False)
    crud.create_user(db, driver_example)

    reg = crud.is_registered(db, driver_id)
    assert (reg)


def test_user_not_in_db():
    db = mongomock.MongoClient().db
    driver_id = "123"
    reg = crud.is_registered(db, driver_id)
    assert (not reg)


def test_get_roles():
    db = mongomock.MongoClient().db
    driver_id = "10"
    name_asked = "Santix"
    roles = ["Driver"]

    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", roles=roles,
                                             car=car_example, is_blocked=False)
    crud.create_user(db, driver_example)

    roles_obtained = crud.get_roles(db, driver_id)
    assert (set(roles_obtained) == set(roles))


def test_get_multiple_roles():
    db = mongomock.MongoClient().db
    driver_id = "10"
    name_asked = "Santix"
    roles = ["Driver"]

    car_example = users_schema.CarBase(model="Reno12", year=2012,
                                       plaque="AA800BB", capacity=5)
    driver_example = users_schema.DriverBase(id=driver_id, name=name_asked,
                                             last_name="F", roles=roles,
                                             car=car_example, is_blocked=False)
    crud.create_user(db, driver_example)

    roles_obtained = crud.get_roles(db, driver_id)
    assert (set(roles_obtained) == set(roles))

    changes = {"roles": ["Passenger"], "address": "asd"}
    crud.update_user(db, driver_id, changes=changes)
    roles_obtained = crud.get_roles(db, driver_id)
    assert (set(roles_obtained) == set(["Driver", "Passenger"]))
