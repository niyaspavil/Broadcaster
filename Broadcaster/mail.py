from .plugin import Plugin, PluginError
import tweepy
from .dummy_engine import Engine
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class mail(plugin):

	  def __init__(self,msg):
        """Constructor for mail class. The msg is the content to be mailed to the others"""
        
	self.msg=msg
	self.state="waiting"
	try:
            self.engine=Engine()
        except Exception:
            raise PluginError(PluginError.ERROR)
	try:
		self.server = smtplib.SMTP('smtp.gmail.com:587')    
		self.server.ehlo()
		self.server.starttls()
	except Exception:
	     raise PluginError(pluginError.ERROR)
	
	def post(self):
        """Method to invoke plugin to post message to site"""
        raise NotImplementedError()

    def status(self):
        """Method to query status of the plugin activity"""
        raise NotImplementedError()

    def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()
