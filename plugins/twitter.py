from ..Broadcaster.plugin import Plugin, PluginError
from ..Broadcaster.dummy_engine import Engine
import tweepy

__plugin_name__="twitter"

class twitter(Plugin):
    """plugin tweets msg to twitter"""
    
    def __init__(self,msg):
        """initialise and set message recieved for post"""

        if len(msg)>160:
            raise PluginError(PluginError.VALID_ERROR)
        self.msg=msg
        self.auth_url="https://apps.twitter.com"
        self.state="waiting"
	self.reset_user=False
	self.reset_consumer=False
        try:
            self.engine=Engine(__plugin_name__)
        except Exception:
            raise PluginError(PluginError.ERROR)
        self.auth=None

    def post(self):
        """Method to invoke plugin to post message to site"""
        self.state="authenticating"
        try:
            api=self.pre_auth()
        except tweepy.TweepError as error:
            self.error_handler(0, error)
        self.state="publishing"
        try:
            api.update_status(self.msg)
        except tweepy.TweepError as error:
            self.error_handler(1, error)
        self.state="done"
        return True

    def status(self):
        """Method to query status of the plugin activity"""
        return self.state

    def pre_auth(self):
        """This method gets the user and developer authentication via tweetpy api and return tweepy api object"""
        consumer_key,consumer_secret=self.get_consumer_keys()
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        user_token,user_token_secret=self.get_user_keys()
        self.auth.set_access_token(user_token, user_token_secret)
        return tweepy.API(self.auth)

    def get_consumer_keys(self):
        """retrieve keys from engine and return in list as [consumer_key,consumer_secret]"""
	
        key=self.engine.get_attrib('consumer_key')
        secret=self.engine.get_attrib('consumer_secret')
        if key=='' or secret=='' or self.reset_consumer:
            self.state="waiting for consumer keys"
            self.engine.prompt_user("Visit the %s and create a twitter application with read and write permission" % (self.auth_url), None)
            key=self.engine.prompt_user("Enter app key", str)
            secret=self.engine.prompt_user("Enter app secret", str)
            self.engine.set_attrib('consumer_key', key)
            self.engine.set_attrib('consumer_secret', secret)
            self.reset_consumer=False
        self.state="authenticating"
        return [key, secret]

    def get_user_keys(self):
        """retrieve keys from engine and return in list as [user_key,user_secret]"""

        token=self.engine.get_attrib('user_token')
        secret=self.engine.get_attrib('user_token_secret')
        if token=='' or secret=='' or self.reset_user:
            self.state="waiting for user keys"
            self.auth_url = self.auth.get_authorization_url()
            pin=self.engine.prompt_user("Visit the %s and enter the authorization pin" %(self.auth_url), int)
            self.auth.get_access_token(pin)
            token=self.auth.access_token.key
            secret=self.auth.access_token.secret
            self.engine.set_attrib('user_token',token)
            self.engine.set_attrib('user_token_secret',secret)
            self.reset_user=False
        self.state="authenticating"
        return [token, secret]

    def error_handler(self, level, error):
        if type(error.response)==None:
            raise PluginError(PluginError.NET_ERROR)
        elif str(error.response.status).startswith("5"):
            raise PluginError(PluginError.SERV_ERROR)
        elif error.response.status<400:
            raise PluginError(PluginError.SERV_ERROR)
        elif level==1:
            self.handle_user(error)
        elif level==0:
            self.handle_consumer(error)
        else:
            raise PluginError(PluginError.ERROR)

    def handle_user(self, error):
        if error.message[0]["code"]==187:
            raise PluginError(PluginError.VALID_ERROR)
        elif error.message[0]["code"]==185:
            raise PluginError(PluginError.SERV_ERROR)
        elif error.message[0]["code"]==261:
            raise PluginError(PluginError.SERV_ERROR)
        elif error.message[0]["code"]==226:
            raise PluginError(PluginError.SERV_ERROR)
        elif error.message[0]["code"]==215:
            self.reset_user=True
            self.reset_consumer=True
            self.post()
        elif error.message[0]["code"]==32 or error.message[0]["code"]==89 or error.message[0]["code"]==135:
            self.reset_user=True
            self.post()
        else:
            raise PluginError(PluginError.ERROR)

    def handle_consumer(self, error):
        if error.response.status==401:
            self.reset_consumer=True
            self.reset_user=True
            self.post()
        else:
            raise PluginError(PluginError.ERROR)
