from .plugin import Plugin, PluginError
from .dummy_engine import Engine
import datetime
import xmlrpclib

class blog():

    def __init__(self,msg):
        """Constructor for mail class. The msg is the content to be mailed to the others"""
        
        self.msg=msg
        self.username= None
        self.state="waiting"
        self.name = "blog"
        try:
            self.engine=Engine()
        except Exception:
            raise PluginError(PluginError.ERROR)
