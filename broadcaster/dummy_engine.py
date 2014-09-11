import ConfigParser
import importlib
import os.path
import glob
from os.path import basename, splitext, expanduser, sep
import os

plugins_dir = "./broadcaster/plugins"
private_home=expanduser("~")+sep+".Broadcaster"
cfgfile=private_home+sep+"conf.ini"
pkg="broadcaster.plugins"
__all_chnl__=None
UI=None
debug_mode=False

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

    def prompt_user(self, msg, type=None, debug=False):
        """prompts user with msg and return the input from user"""
        if debug and (not debug_mode):
            return None
        else:
            return self.UI.prompt(msg, type)
        

def broadcast(msg, chnl_list, mode, ui):
    global UI,__all_chnl__,debug_mode
    UI=ui
    debug_mode=mode
    dict={}
    __all_chnl__=get_chnls()
    for chnl in chnl_list:
        if has_channel(chnl):
            plug=load_plugin(chnl, msg)
            try:
                plug.post()
                dict[chnl]="Successful"
            except Exception:
                dict[chnl]="Failed"
        else:
            dict[chnl]="Failed: Plugin not found..\n To add new plugin, insert plugin file to broadcaster/plugins"
    return dict

def get_chnls():
    plugins = []
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
    engine=Engine(chnl)
    mod=importlib.import_module("."+chnl,pkg)
    return getattr(mod,chnl)(engine, msg)

def reset_plugin(chnls):
    try:
        dict={}
        if os.path.isfile(cfgfile):
            conf=ConfigParser.ConfigParser()
            conf.read(cfgfile)
            for chnl in chnls:
                if conf.has_section(chnl):
                    conf.remove_section(chnl)
                    dict[chnl]="reset"
                else:
                    dict[chnl]="no data to reset"
            conf.write(open(cfgfile,"w"))
        else:
            dict["all-channel"]="no data to reset"
        return dict
    except Exception:
        return {"all-channel":"reset failed"}
                
