class Plugin(object):
    """Provides abstract class for loaded plugins of each sites"""

    def __init__(self,msg):
        """Constructor for Plugin class. The msg is the content to be posted to the site like tweet for twitter etc"""
        raise NotImplementedError()

    def post(self):
        """Method to invoke plugin to post message to site"""
        raise NotImplementedError()

    def status(self):
        """Method to query status of the plugin activity"""
        raise NotImplementedError()

    def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()

class PluginError(Exception):
    """custom exception for plugins"""

    def __init__(self, code):
        """error code:....
        0x01 ->  message errors
        0x02 ->  network errors
        0x03 ->  authenticate errors
        0x04 ->  conf errors"""
        self.code=code
