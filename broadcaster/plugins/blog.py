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

    def pre_authenticate(self):
        """This method create a server objct and user names and password"""
        wp_url=self.engine.get_attrib('wp_url',self.name)
        if wp_url=='' or wp_url==None:
            self.state="waiting for wordpress url detials"
            wp_url=self.engine.prompt_user("Enter wordpress url", str)
            self.engine.set_attrib('wp_url',wp_url,self.name)
        wp_url  = wp_url+"/xmlrpc.php"
        try:
            self.server = xmlrpclib.ServerProxy(wp_url)
        except:
            print "server error"
        user_name,user_password=self.get_consumer_details()
        self.username = user_name
        self.password = user_password
        return True 
