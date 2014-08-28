import ConfigParser

cfgfile="conf.ini"

class Engine(object):
    """class engine for plugins"""
    
    def __init__(self):
        """identifying plugin and setting-up conf"""
        self.plugin="twitter"
        self.conf=ConfigParser.ConfigParser()
        conf.read(cfgfile)
        self.mock_input=''

    def get_attrib(self, option):
        """return attribute from conf"""
        if self.conf.has_option(self.plugin, option):
            value=self.conf.get(self.plugin,option)
        else:
            value=""
        return value

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        if not self.conf.has_section(self.plugin):
            self.conf.add_section(self.plugin)
        self.conf.set(self.plugin, option, value)
        self.conf.write(open(cfgfile,"w"))

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return self.mock_input

def broadcast(msg, chnl_list):
    for chnl in chnl_list:
        if has_channel(chnl):
            plug=load_plugin(chnl, msg)
            plug.post()

def has_channel(chnl):
    tmp_engine=Engine()
    tmp_engine.plugin="general"
    all_chnl=tmp_engine.get_attrib("channels").split()
    if chnl in all_chnl:
        return True
    else:
        return False

def load_plugin(chnl, msg):
    retutn getattrib(__import__(chnl),chnl)(msg)
