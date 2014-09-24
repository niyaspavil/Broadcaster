import ConfigParser
import importlib
import os.path
import glob
from os.path import basename, splitext, expanduser, sep
import os

__plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"
__private_home__=expanduser("~")+sep+".Broadcaster"
__pkg__="broadcaster.plugins"
__cfgfile__=__private_home__+sep+"conf.ini"
__conf__=None
__all_chnl__=None
__ui__=None
__debug_mode__=False

#some input type standards from engine
INPUT_TYPE_NONE="none"
INPUT_TYPE_NUMBER="number"
INPUT_TYPE_TEXT_ONELINE="text:oneline"
INPUT_TYPE_TEXT_MULTILINE="text:multiline"
INPUT_TYPE_TEXT_PASSWORD="text:password"

class Engine(object):
    """Provides the methods required by plugins for persistent storage
    and retrieval of data and user interactions. An instance of this
    class is passed to each plugin when it is loaded"""
    
    def __init__(self, plugin):
        """identifying plugin and and binds UI"""
        self.section=plugin
	self.UI=__ui__

    def get_attrib(self, option):
        """returns requested attribute from conf. if unavailable empty
        string is returned"""
 	if __conf__.has_option(self.section,option):
            value=__conf__.get(self.section,option)
        else:
            value=""
        return value

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        global __conf__
        if not __conf__.has_section(self.section):
            __conf__.add_section(self.section)
        __conf__.set(self.section, option, value)

    def prompt_user(self, msg, type=None, debug=False):
        """prompts user with msg and return the input from user based
        on debug flag"""
        if debug and (not __debug_mode__):
            return None
        else:
            return self.UI.prompt(self.section+"->\n"+msg, type)
        

def broadcast(msg, sent_via, mode, ui):
    """Provides the basic method which enable broadcasting the message
    to requested channels using the plugins.
    msg --> user message to be broadcasted
    sent_via --> list of channel,user tuples to which broadcast is to be made
    mode --> debug mode(boolean)
    ui --> UI object which is able to handle requests and responses from engine"""
    global __ui__, __all_chnl__, __debug_mode__, __conf__
    __ui__=ui
    __debug_mode__=mode
    dict={}
    __all_chnl__=get_channels()
    __conf__=get_conf()
    for chnl, user in sent_via:
        if has_channel(chnl):
            plug=load_plugin(chnl, user, msg)
            try:
                plug.post()
                dict[chnl+":"+user]="Successful"
            except Exception as x:
                dict[chnl+":"+user]="Failed ::-> "+x.message
        else:
            dict[chnl+":"+user]="Failed: Plugin not found..\n To add new plugin, insert plugin file to "+__plugins_dir__
    set_conf(__conf__)
    return dict

def get_channels():
    """returns list of available channel/plugins by searching
    plugin directory"""
    plugins = []
    plugin_files = glob.glob("{}/*.py".format(__plugins_dir__))
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

def load_plugin(chnl, user, msg):
    """loads and returns the plugin object"""
    if user.strip()=='':
        user=get_default_user()
        return load_plugin(chnl, user, msg)
    engine=Engine(chnl+':'+user)
    mod=importlib.import_module("."+chnl, __pkg__)
    return getattr(mod,chnl)(engine, msg)

def get_conf():
    """returns ConfigParser object after initialising with contents of
    configuration file"""
    conf=ConfigParser.ConfigParser()
    conf.read(__cfgfile__)
    return conf

def set_conf(conf):
    """saves the ConfigParser object contents to configuration file"""
    try:
        if not os.path.isfile(__cfgfile__):
            if not os.path.exists(__private_home__):
                os.makedirs(__private_home__)
        conf_file=open(__cfgfile__,"w")
        conf.write(conf_file)
        conf_file.close()
        return True
    except Exception:
        return False

def get_default_user():
    """returns default user name from conf if set else requests and returns from user through registered ui object"""
    engine=Engine("defaults")
    user=engine.get_attrib("user")
    if user.strip()=='':
        user=engine.prompt_user("Enter a default username for sent profile", str)
        engine.set_attrib("user", user)
    return user

def reset_channels(chnls):
    """Provides the facility to reset configuration data of each
    plugins passed"""
    try:
        dict={}
        if os.path.isfile(__cfgfile__):
            if chnls==[("all","")]:
                os.remove(__cfgfile__)
                return {"all-channel":"reset success"}
            conf=ConfigParser.ConfigParser()
            conf.read(__cfgfile__)
            for chnl, user in chnls:
                if user.strip=='':
                    user=find_default_user(conf)
                section=chnl+":"+user
                if conf.has_section(section):
                    conf.remove_section(section)
                    dict[section]="reset success"
                else:
                    dict[section]="no data to reset"
            conf.write(open(__cfgfile__,"w"))
        else:
            dict["all-channel"]="no data to reset"
        return dict
    except Exception:
        return {"all-channel":"reset failed"}
                
def find_default_user(conf):
    if conf.has_option("default", "user"):
        return conf.has_option("default", "user")
    else:
        return ""
