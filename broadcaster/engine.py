#module engine

def add_user(name):
    """creates a new user with username name(type str) and throws UserException on failure"""
    pass

def set_default_user(name):
    """set the default username as name(type str). If no such user exists, UserException is thrown"""
    pass

def get_default_user():
    """returns the default username as a string. If unset UserException is thrown"""
    pass

def get_all_users():
    """returns the list of all existing usernames"""
    return ["test_user1","test_user2"]

def delete_user(name):
    """removes the existing user and associated data for username name. Throws UserException on failure"""
    pass
