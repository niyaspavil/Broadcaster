import ConfigParser
import importlib
import os.path

cfgfile="conf.ini"
UI=None
class Engine(object):
    """class engine for plugins"""
    
    def __init__(self):
        """identifying plugin and setting-up conf"""
        self.section=" "
        self.conf=ConfigParser.ConfigParser()
	self.UI=UI
        if not os.path.isfile(cfgfile):
            conf_file=open(cfgfile,"w")
            self.conf.add_section("general")
            conf.set("general","plugins","")
            conf_file.close()

    def get_attrib(self, option,section):
        """return attribute from conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
	self.section = section
 	if self.conf.has_option(self.section,option):
            value=self.conf.get(self.section,option)
        else:
            value=""
        return value

    def set_attrib(self, option, value,section):
        """stores option-value pair to the conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
	self.section = section
        if not self.conf.has_section(self.section):
            self.conf.add_section(self.section)
        self.conf.set(self.section, option, value)
        self.conf.write(open(cfgfile,"w"))

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return self.UI.prompt(msg)

def broadcast(msg, chnl_list, ui):
    global UI
    UI=ui
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
    all_chnl=tmp_engine.get_attrib('plugins','general').split()
    if chnl in all_chnl:
        return True
    else:
        return False

def load_plugin(chnl, msg):
    mod=importlib.import_module("."+chnl,"Broadcaster.Broadcaster")
    return getattr(mod,chnl)(msg)
