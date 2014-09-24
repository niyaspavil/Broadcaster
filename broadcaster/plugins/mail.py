from ..plugin import Plugin, PluginError
from .. import engine
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib
__plugin_name__="mail"


class mail(Plugin):

    def __init__(self, engine, msg):
        """Constructor for mail class. The msg is the content to be mailed to the others"""
        self.engine=engine
	self.msg=msg
	self.username= None
	self.state="waiting"
	self.To_mail=[]
	self.name = "mail"
        self.reset_user=False
	
		
    def post(self):
        """Method to send mail"""
        self.state="authenticating"
	self.retry=3
        while self.retry:
	    try:
                self.pre_authenticate()
            except smtplib.SMTPAuthenticationError as error:
		self.engine.prompt_user(
		    "Invalid user name or password else check your security level", engine.INPUT_TYPE_NONE, False)
	        self.engine.prompt_user(error.__str__(), engine.INPUT_TYPE_NONE, True)
		self.retry-=1
                self.reset_user=True
		continue
            except Exception as e:
		self.engine.prompt_user("--Unable to connect to internet--", engine.INPUT_TYPE_NONE, True)
                raise PluginError(PluginError.NET_ERROR)
        	continue

	    mail=self.compose_mail()
	    fromAddr = self.username
	    self.retry-=1	
	    for toAddr in self.To_mail:
	        try:
                    self.server.sendmail(fromAddr, toAddr,mail)
                    self.state="done"
		    self.engine.prompt_user("sended mail to  "+ toAddr, engine.INPUT_TYPE_NONE, False)			
		    continue
	        except smtplib.SMTPRecipientsRefused as error:
		    self.engine.prompt_user(
                        "Invalid Recipient Address  "+toAddr, engine.INPUT_TYPE_NONE, False)
	            self.engine.prompt_user(error.__str__(), engine.INPUT_TYPE_NONE, True)
                    self.retry-=1
		    continue
                except smtplib.SMTPDataError as error:
		    self.engine.prompt_user(error.__str__(), engine.INPUT_TYPE_NONE, True)
                    self.retry-=1
                    continue
                except smtplib.SMTPConnectError as error:
		    self.engine.prompt_user("--Unable to connect to internet--", engine.INPUT_TYPE_NONE, True)
		    raise PluginError(PluginError.NET_ERROR)
                    continue
		print toAddr
            if toAddr == self.To_mail[-1] and self.state == 'done':
                return True
	    else:
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
        if usrname == '' or passwd =='' or usrname == None or passwd == None or self.reset_user:
            self.state="waiting for consumer detials"
            usrname=self.engine.prompt_user("Enter username", engine.INPUT_TYPE_TEXT_ONELINE,False)
       	    passwd=self.engine.prompt_user("Enter password", engine.INPUT_TYPE_TEXT_PASSWORD,False)
            self.engine.set_attrib('user_name', usrname)
       	    self.engine.set_attrib('user_password', passwd)
       	self.state="authenticated"
        return [usrname, passwd]


    def compose_mail(self):
        """this function composes mail"""
	to = self.engine.prompt_user("To",engine.INPUT_TYPE_TEXT_ONELINE,False)
	self.To_mail = to.split()
	subject=self.engine.prompt_user("Subject",engine.INPUT_TYPE_TEXT_ONELINE,False)
	contents=self.engine.prompt_user(
             "This is your message '{}' .press enter for continue, else type content".format(self.msg),engine.INPUT_TYPE_TEXT_MULTILINE,False)
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
