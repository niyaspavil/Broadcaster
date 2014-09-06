import ConfigParser
import importlib
import os.path
import glob
from os.path import basename, splitext, expanduser, sep
import os

plugins_dir = "./Broadcaster/plugins"
private_home=expanduser("~")+sep+".Broadcaster"
cfgfile=private_home+sep+"conf.ini"
__all_chnl__=None
UI=None

class Engine(object):
    """class engine for plugins"""
    
    def __init__(self, plugin):
        """identifying plugin and setting-up conf"""
        self.section=plugin
        self.conf=ConfigParser.ConfigParser()
	self.UI=UI
        if not os.path.isfile(cfgfile):
            if not os.path.exists(private_home):
                os.makedirs(private_home)
            open(cfgfile,"w").close()

    def get_attrib(self, option):
        """return attribute from conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
 	if self.conf.has_option(self.section,option):
            value=self.conf.get(self.section,option)
        else:
            value=""
        return value

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        self.conf.__init__()
        self.conf.read(cfgfile)
        if not self.conf.has_section(self.section):
            self.conf.add_section(self.section)
        self.conf.set(self.section, option, value)
        self.conf.write(open(cfgfile,"w"))

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return self.UI.prompt(msg, type)

def broadcast(msg, chnl_list,debug, ui):
    global UI,__all_chnl__
    UI=ui
    dict={}
    __all_chnl__=find_chnls()
    for chnl in chnl_list:
        if has_channel(chnl):
            plug=load_plugin(chnl, msg)
            try:
                plug.post()
                dict[chnl]="Successful"
            except Exception:
                dict[chnl]="Failed"
        else:
            dict[chnl]="Failed: Plugin not found..\n To add new plugin, insert plugin file to Broadcaster/plugins"
    return dict

def find_chnls():
    plugins = []
    print plugins_dir
    plugin_files = glob.glob("{}/*.py".format(plugins_dir))
    for plugin_file in plugin_files:
        if plugin_file.endswith("__init__.py"):
            continue
        name, ext = splitext(basename(plugin_file))
        plugins.append(name)
    return plugins

def has_channel(chnl):
    if chnl in __all_chnl__:
        return True
    else:
        return False

def load_plugin(chnl, msg):
    mod=importlib.import_module("."+chnl,"Broadcaster.plugins")
    return getattr(mod,chnl)(msg)
