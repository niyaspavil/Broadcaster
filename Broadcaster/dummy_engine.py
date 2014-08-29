import ConfigParser
import importlib
import os.path

cfgfile="conf.ini"

class Engine(object):
    """class engine for plugins"""
    
    def __init__(self):
        """identifying plugin and setting-up conf"""
        self.plugin="twitter"
        self.conf=ConfigParser.ConfigParser()
        if not os.path.isfile(cfgfile):
            conf_file=open(cfgfile,"w")
            self.conf.add_section("general")
            conf.set("general","plugins","")
            conf_file.close()

    def get_attrib(self, option):
        """return attribute from conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
        if self.conf.has_option(self.plugin, option):
            value=self.conf.get(self.plugin,option)
        else:
            value=""
        return value

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
        if not self.conf.has_section(self.plugin):
            self.conf.add_section(self.plugin)
        self.conf.set(self.plugin, option, value)
        self.conf.write(open(cfgfile,"w"))

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return self.mock_input

def broadcast(msg, chnl_list, ui):
    dict={}
    for chnl in chnl_list:
        if has_channel(chnl):
            plug=load_plugin(chnl, msg)
            try:
                plug.post()
                dict[chnl]="Successful"
            except Exception:
                dict[chnl]="Failed"
        else:
            dict[chnl]="Failed: Plugin not found..\n Add plugin file to Broadcaster/Broadcaster and add module name to conf.ini:-->general->plugins section (use blank space to seperate module names)"
    return dict

def has_channel(chnl):
    tmp_engine=Engine()
    tmp_engine.plugin="general"
    all_chnl=tmp_engine.get_attrib("plugins").split()
    if chnl in all_chnl:
        return True
    else:
        return False

def load_plugin(chnl, msg):
    mod=importlib.import_module("."+chnl,"Broadcaster.Broadcaster")
    return getattr(mod,chnl)(msg)
