from .. import engine

#testing user related functions

def test_get_all_users():
    engine.add_user("test_user1")
    engine.add_user("test_user2")
    all_users=engine.get_all_users()
    engine.delete_user("test_user1")
    engine.delete_user("test_user2")

def test_get_default_user():
    engine.get_default_user()
    engine.add_user("test_user")
    engine.set_default_user("test_user")
    engine.get_default_user()
    engine.delete_user("test_user")

def test_add_user():
    engine.add_user("test_user")
    engine.add_user("test_user")
    engine.delete_user("test_user")

def test_set_default_user():
    engine.set_default_user("test_user")
    engine.add_user("test_user")
    engine.set_default_user("test_user")
    engine.delete_user("test_user")

def test_delete_user():
    engine.delete_user("test_user")
    engine.add_user("test_user")
    engine.delete_user("test_user")

#Data

def test_data():
    data=engine.Data()
    data.set("test_key","test_value")
    val=data.get("test_key")
    assert val=="test_value"
