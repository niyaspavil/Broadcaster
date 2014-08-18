import ConfigParser

class Engine(object):
    """Mocker class for engine"""
    
    def __init__(self):
        """nothing special... :P"""
        self.plugin="twitter"

    def get_attrib(self, option):
        """return attribute from conf.ini"""
        config=ConfigParser.ConfigParser()
        config.read("../conf.ini")
        return config.get(self.plugin, option)
