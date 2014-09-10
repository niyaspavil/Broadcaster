
class Engine(object):
    """Mocker class for engine"""
    
    def __init__(self, plugin):
        """identifying plugin and setting-up conf"""
        self.plugin=plugin
        self.conf={}
        self.mock_input=''

    def get_attrib(self, option):
        """return attribute from conf"""
        if self.conf.get(option):
		return self.conf.get(option)
	else:
		return ""

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        self.conf[option]=value

    def prompt_user(self, msg, type=None, debug=None):
        """prompts user with msg and return the input from user"""
        return self.mock_input

def broadcast(msg,chanl,debug,ui):
	return {"plugin":"test"}

def get_chnls():
	return ['mail','twitter']
