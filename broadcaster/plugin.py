
class Plugin(object):
    """abstract class providing necessary methods needed for proper implementation on plugins"""

    def __init__(self, data):
        """data recieves the data object containing persistant data associated to the initialised plugin for the current use"""
        raise NotImplementedError()

    def get_auth_fields(self):
        """this method should return the fields required to authenticate the plugin as array of engine's field objects."""
        raise NotImplementedError()

    def get_post_fields(self):
        """this method should return the fields required to post as array of engine's field objects."""
        raise NotImplementedError()

    def authenticate(self, input):
        """should authenticate plugin based on the input fields passed on user behalf and returns the status object """
        raise NotImplementedError()

    def post(self, input):
        """posts the content and returns the status object"""
        raise NotImplementedError()
