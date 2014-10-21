
class User(object):
    """user abstraction which includes username, list of authenticated
    plugins and associated methods to modify it"""

    def __init__(self, name):
        pass

    def get_plugins(self):
        pass

    def add_plugin(self, plugin, data):
        pass

    def remove_plugin(self, plugin):
        pass


class Field(object):
    """Class to specify input parameters or fields."""

    def __init__(self, **kwargs):
        pass


class Data(object):
    """class to represent data object with getters and setters for
    keys"""

    def __init__(self):
        pass

    def get(self, key):
        pass

    def set(self, key, value):
        pass


class Status(object):
    """"""

    def __init__(self):
        pass


def add_user(name):
    """creates a new user with username name(type str) and throws
    UserException on failure"""
    pass

def set_default_user(name):
    """set the default username as name(type str). If no such user
    exists, UserException is thrown"""
    pass

def get_default_user():
    """returns the default username as a string. If unset
    UserException is thrown"""
    pass

def get_all_users():
    """returns the list of all existing usernames"""
    pass

def delete_user(name):
    """removes the existing user and associated data for username
    name. Throws UserException on failure"""
    pass

def get_all_plugins():
    """returns an array of installed plugin names"""
    pass

def get_plugin_fields(plugin, auth_field=False):
    """returns an array of field objects specifying input data required for plugin. If auth flag is set, data fields for authourizing plugin is returned and fields for posting data on the other case."""

def broadcast(user, send_data):
    """this method does the broadcasting of message via plugins. The
    argument send_data should be a list of 3-tuples like (user, plugin, data), where user
    and plugin stands for names of type str and data is the object of
    class Data and must contain keys and values for fields of
    corresponding plugin """
    pass
