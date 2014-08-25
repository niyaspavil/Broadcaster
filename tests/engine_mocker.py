
class Engine(object):
    """Mocker class for engine"""
    
    def __init__(self):
        """identifying plugin and setting-up conf"""
        self.plugin="twitter"
        self.conf={}
        self.mock_input=''

    def get_attrib(self, option):
        """return attribute from conf"""
        return self.conf.get(option)

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        self.conf[option]=value

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return self.mock_input


