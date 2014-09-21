from ..plugin import Plugin, PluginError
import tweepy
from .. import engine
__plugin_name__="twitter"

class twitter(Plugin):
    """plugin tweets msg to twitter"""
    
    def __init__(self, engine, msg):
        """initialise and set message recieved for post"""

        if len(msg)>160:
            raise PluginError(PluginError.VALID_ERROR)
	self.engine=engine
        self.msg=msg
        self.auth_url="https://apps.twitter.com"
        self.state="waiting"
	self.reset_user=False
	self.reset_consumer=False

    def post(self):
        """Method to invoke plugin to post message to site"""
	self.retry=3
        while self.retry:
            self.state="authenticating"
            try:
                api=self.pre_auth()
            except tweepy.TweepError as error:
                self.error_handler(error, 1)
		self.retry-=1
                continue
            self.state="publishing"
            try:
                api.update_status(self.msg)
                self.state="done"
                return True
            except tweepy.TweepError as error:
                self.error_handler(error, 0)
		self.retry-=1
                continue
	raise PluginError(PluginError.AUTH_ERROR)

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
        """retrieve twitter application keys through engine and return in list as [consumer_key,consumer_secret]"""
	
        key=self.engine.get_attrib('consumer_key')
        secret=self.engine.get_attrib('consumer_secret')
        if key=='' or secret=='' or self.reset_consumer:
            self.state="waiting for consumer keys"
            self.engine.prompt_user("Visit the %s and create a twitter application with read and write permission" %(self.auth_url),engine.INPUT_TYPE_NONE)
            key=self.engine.prompt_user("Enter app key",engine.INPUT_TYPE_TEXT_ONELINE)
            secret=self.engine.prompt_user("Enter app secret",engine.INPUT_TYPE_TEXT_ONELINE)
            self.engine.set_attrib('consumer_key', key)
            self.engine.set_attrib('consumer_secret', secret)
            self.reset_consumer=False
        self.state="authenticating"
        return [key, secret]

    def get_user_keys(self):
        """retrieve user auth keys through engine and return in list as [user_key,user_secret]"""

        token=self.engine.get_attrib('user_token')
        secret=self.engine.get_attrib('user_token_secret')
        if token=='' or secret=='' or self.reset_user:
            self.state="waiting for user keys"
            self.auth_url = self.auth.get_authorization_url()
            pin=self.engine.prompt_user("Visit the %s and enter the authorization pin" %(self.auth_url),engine.INPUT_TYPE_NUMBER)
            try:
                self.auth.get_access_token(pin)
            except tweepy.TweepError as error:
                self.engine.prompt_user("entered pin is wrong",engine.INPUT_TYPE_NONE,True)
                raise PluginError(PluginError.ERROR)
            token=self.auth.access_token.key
            secret=self.auth.access_token.secret
            self.engine.set_attrib('user_token',token)
            self.engine.set_attrib('user_token_secret',secret)
            self.reset_user=False
        self.state="authenticating"
        return [token, secret]

    def error_handler(self, error, level):
        """primary error handle which analyse tweepy exceptions and decides whether to raise exception or handle internally. This handler highly relies on error codes passed by tweepy from twitter."""
        self.engine.prompt_user(error.__str__(),engine.INPUT_TYPE_NONE, True)
        if type(error.message)==str:
            self.engine.prompt_user("--Unable to connect to internet--",engine.INPUT_TYPE_NONE, True)
            raise PluginError(PluginError.NET_ERROR)
        elif level==0:
            return self.user_handler(error)
        elif level==1:
            return self.consumer_handler(error)
        else:
            self.engine.prompt_user("--exception unhandled by plugin--", __INPUT_TYPE_NONE__, True)
            raise PluginError(PluginError.ERROR)

    def user_handler(self, error):
        """exception handler which identifies auth key errors and flags for reset user keys"""
        if error.message[0]["code"]==32 or error.message[0]["code"]==89 or error.message[0]["code"]==215:
            self.engine.prompt_user("--resetting user keys--", engine.INPUT_TYPE_NONE, True)
            self.reset_user=True
        elif error.message[0]["code"]==187:
            raise PluginError("Duplicate tweet is not allowed!!")
        else:
            self.engine.prompt_user("--exception unhandled at user_handler--",engine.INPUT_TYPE_NONE, True)
            raise PluginError(PluginError.ERROR)
            
    def consumer_handler(self, error):
        """handler which sets flag to reset application keys and user keys """
        self.engine.prompt_user("--resetting consumer keys--",engine.INPUT_TYPE_NONE, True)
        self.reset_consumer=True
        self.reset_user=True
        
