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
	        """Method to send mail"""
                self.state="authenticating"
	
		try:
           		api=self.pre_authenticate()
        	except Exception:
            		raise PluginError(PluginError.AUTH_ERROR)	
		
    def status(self):
        """Method to query status of the plugin activity"""
        raise NotImplementedError()

    def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()




	def pre_authenticate(self):
        """This method gets username and password """
        user_name,user_password=self.get_consumer_details()
        self.server.login(user_name, user_password)
        return True 






	def get_consumer_details(self):
        """retrieve user details from engine and return in list as [user_name,user_password]"""
	
        usrname=self.engine.get_attrib('user_name')
        psswd=self.engine.get_attrib('user_password')
        if usrname=='' or passwd=='' or usrname==None or passwd==None:
            self.state="waiting for consumer detials"
            usrname=self.engine.prompt_user("Enter username", str)
            passwd=self.engine.prompt_user("Enter password", str)
            self.engine.set_attrib('user_name', usrname)
            self.engine.set_attrib('user_password', passwd)
        self.state="authenticating"
        return [usrname, passwd]

