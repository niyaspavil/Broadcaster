from .plugin import Plugin, PluginError
import tweepy
from .dummy_engine import Engine
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class mail(plugin):

	  def __init__(self,msg):
        	"""Constructor for mail class. The msg is the content to be mailed to the others"""
        
		self.msg=msg
		self.username= None
		self.state="waiting"
		self.To_mail=[]
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
           		self.pre_authenticate()
        	except Exception:
            		raise PluginError(PluginError.AUTH_ERROR)
		mail=self.compose_mail()
		
		for toAddr in To_Email:
			try:
				self.server.sendmail(fromAddr, toAddr, mail)
				response[toAddr] = 'Mail Sent		
		return True

		
	def status(self):
        	"""Method to query status of the plugin activity"""
        	raise NotImplementedError()

	def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()




	def pre_authenticate(self):
        """This method gets username and password """
        user_name,user_password=self.get_consumer_details()
	self.username = user_name
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


	def compose_mail(self):
		"""this function composes mail"""

		to=self.engine.prompt_user("To").split()
		self.To_mail = to
		subject=self.engine.prompt_user("Subject",str)
		contents=self.engine.prompt_user("This is your message {} .press enter for continue, else type content".format{self.msg},str)
		if contents:
			message = contents
		else:
			message = self.msg
		mail = MIMEMultipart()
		mail['From'] = self.username
		mail['To'] = to
		mail['Subject'] = subject
		mail.attach(MIMEText(message, 'plain'))
		return mail.as_string()
		
