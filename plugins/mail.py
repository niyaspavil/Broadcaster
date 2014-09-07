from ..Broadcaster.plugin import Plugin, PluginError
from ..Broadcaster.dummy_engine import Engine
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib
import socket
__plugin_name__="mail"


class mail(Plugin):

    def __init__(self,msg):
        """Constructor for mail class. The msg is the content to be mailed to the others"""
        
	self.msg=msg
	self.username= None
	self.state="waiting"
	self.To_mail=[]
	self.name = "mail"
        self.reset_user=False
	try:
            self.engine=Engine(__plugin_name__)
	except Exception:
	    raise PluginError(PluginError.ERROR)
	
		
    def post(self):
        """Method to send mail"""
        self.state="authenticating"
	self.retry=3
        while self.retry:
	    try:
                self.pre_authenticate()
            except smtplib.SMTPAuthenticationError as error:
	        self.engine.prompt_user(error.__str__(), None, True)
		self.retry-=1
		continue
            except socket.giaerror:
		self.engine.prompt_user("--Unable to connect to internet--", None, True)

                raise PluginError(PluginError.NET_ERROR)
        	continue

	    mail=self.compose_mail()
	    fromAddr = self.username
		
	    for toAddr in self.To_mail:
	        try:
                    self.server.sendmail(fromAddr, toAddr,mail)
                    self.state="done"
                    return True
	        except smtplib.SMTPRecipientsRefused as error:
	            self.engine.prompt_user(error.__str__(), None, True)
                    self.retry-=1
                    break
                except smtplib.SMTPDataError as error:
		    self.engine.prompt_user(error.__str__(), None, True)
                    self.retry-=1
                    break
                except smtplib.SMTPConnectError as error:
		    self.engine.prompt_user("--Unable to connect to internet--", None, True)
		    raise PluginError(PluginError.NET_ERROR)
                    break
                    
	raise PluginError(PluginError.AUTH_ERROR)		
    def status(self):
        """Method to query status of the plugin activity"""
        return self.state
	



    def pre_authenticate(self):
        """This method create a server object """
	self.server = smtplib.SMTP('smtp.gmail.com',587)    
	self.server.ehlo()
	self.server.starttls()

	user_name,user_password=self.get_user_details()
	self.username = user_name
	     
	self.server.login(user_name, user_password)
	      
        return True 






    def get_user_details(self):
        """retrieve user details from engine and return in list as [user_name,user_password]"""
        usrname=self.engine.get_attrib('user_name')
        passwd=self.engine.get_attrib('user_password')
        if usrname=='' or passwd=='' or usrname==None or passwd==None:
            self.state="waiting for consumer detials"
            usrname=self.engine.prompt_user("Enter username", str,False)
       	    passwd=self.engine.prompt_user("Enter password", str,False)
            self.engine.set_attrib('user_name', usrname)
       	    self.engine.set_attrib('user_password', passwd)
       	self.state="authenticated"
        return [usrname, passwd]


    def compose_mail(self):
        """this function composes mail"""
	to = self.engine.prompt_user("To",str,False)
	self.To_mail = to.split()
	subject=self.engine.prompt_user("Subject",str,False)
	contents=self.engine.prompt_user("This is your message '{}' .press enter for continue, else type content".format(self.msg),str,False)
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
