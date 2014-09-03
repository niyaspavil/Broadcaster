from ..Broadcaster.plugin import Plugin, PluginError
from ..Broadcaster.dummy_engine import Engine
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib

__plugin_name__="mail"


class mail(Plugin):

    def __init__(self,msg):
        """Constructor for mail class. The msg is the content to be mailed to the others"""
        
	self.msg=msg
	self.username= None
	self.state="waiting"
	self.To_mail=[]
	self.name = "mail"
	try:
            self.engine=Engine(__plugin_name__)
	except Exception:
	    raise PluginError(PluginError.ERROR)
	try:
	    self.server = smtplib.SMTP('smtp.gmail.com',587)    
	    self.server.ehlo()
	    self.server.starttls()
	except Exception:
	    raise PluginError(PluginError.ERROR)
		
    def post(self):
        """Method to send mail"""
        self.state="authenticating"
	response = {}
	try:
            self.pre_authenticate()
        except Exception:
            raise PluginError(PluginError.AUTH_ERROR)
	mail=self.compose_mail()
	fromAddr = self.username
		
	for toAddr in self.To_mail:
	    try:
	        self.server.sendmail(fromAddr, toAddr, mail)
		response[toAddr] = 'Mail Sent'
	    except Exception:
	        response[toAddr] = 'Mail Sending Failed'		
            	raise PluginError(PluginError.NET_ERROR)
        self.state="done"
        return True

		
    def status(self):
        """Method to query status of the plugin activity"""
        return self.state
	



    def pre_authenticate(self):
        """This method create a server object """
	user_name,user_password=self.get_consumer_details()
	self.username = user_name
        self.server.login(user_name, user_password)
        return True 






    def get_consumer_details(self):
        """retrieve user details from engine and return in list as [user_name,user_password]"""
        usrname=self.engine.get_attrib('user_name')
        passwd=self.engine.get_attrib('user_password')
        if usrname=='' or passwd=='' or usrname==None or passwd==None:
            self.state="waiting for consumer detials"
            usrname=self.engine.prompt_user("Enter username", str)
       	    passwd=self.engine.prompt_user("Enter password", str)
            self.engine.set_attrib('user_name', usrname)
       	    self.engine.set_attrib('user_password', passwd)
       	self.state="authenticated"
        return [usrname, passwd]


    def compose_mail(self):
        """this function composes mail"""
	to = self.engine.prompt_user("To",str)
	self.To_mail = to.split()
	subject=self.engine.prompt_user("Subject",str)
	contents=self.engine.prompt_user("This is your message '{}' .press enter for continue, else type content".format(self.msg),str)
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
		
