from .plugin import Plugin, PluginError
from .dummy_engine import Engine
import datetime
import xmlrpclib

class blog(Plugin):

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
	def post(self):
	        """Method to post a blog """
                self.state="authenticating"
		try:
           		self.pre_authenticate()
        	except Exception:
            		raise PluginError(PluginError.AUTH_ERROR)
		post=self.compose_post()
		
		try:
			post_id = self.server.metaWeblog.newPost('', self.username, self.password, post, True)
			return True
		except:
			return False
		
	def status(self):
        	"""Method to query status of the plugin activity"""
        	return self.state
	



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






	def get_consumer_details(self):
        	"""retrieve user details from engine and return in list as [user_name,user_password]"""
        	usrname=self.engine.get_attrib('user_name',self.name)
        	passwd=self.engine.get_attrib('user_password',self.name)
        	if usrname=='' or passwd=='' or usrname==None or passwd==None:
        	    self.state="waiting for consumer detials"
        	    usrname=self.engine.prompt_user("Enter username", str)
        	    passwd=self.engine.prompt_user("Enter password", str)
        	    self.engine.set_attrib('user_name', usrname,self.name)
        	    self.engine.set_attrib('user_password', passwd,self.name)
        	self.state="authenticated"
        	return [usrname, passwd]


	def compose_post(self):
		"""this function composes post to blog"""
		title = self.engine.prompt_user("Title",str)
		categories=self.engine.prompt_user("Catogories",str)
		tags=self.engine.prompt_user("Tags",str)
		tags=tags.replace(";",",")
		contents=self.engine.prompt_user("This is your current post '{}' .press enter for continue, else type content".format(self.msg),str)
		if contents:
			message = contents
		else:
			message = self.msg
		date_created = xmlrpclib.DateTime(datetime.datetime.today())
		
		post = {'title': title, 'description': message, 'categories': categories, 'dateCreated': date_created,'mt_keywords': tags}

		return post
