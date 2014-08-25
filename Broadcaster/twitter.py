import plugin
import tweepy
from tests import engine_mocker

class twitter(plugin.plugin):
    """plugin tweets msg to twitter"""
    
    def __init__(self,msg):
        """initialise and set message recieved for post"""
        self.msg=msg
        self.redirect_url="https://apps.twitter.com"
        self.state="waiting"
        self.engine=engine_mocker.Engine()

    def post(self):
        """Method to invoke plugin to post message to site"""
        self.state="authenticating"
        api=self.pre_authenticate()
        self.state="publishing"


##        api.update_status(self.msg)


        self.state="done"
        return True

    def status(self):
        """Method to query status of the plugin activity"""
        return self.state

    def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()

    def pre_authenticate(self):
        """This method gets the user and developer authentication via tweetpy api and return tweepy api object"""
        consumer_key,consumer_secret=self.get_consumer_keys()
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        user_token,user_token_secret=self.get_user_keys()
        auth.set_access_token(user_token, user_token_secret)
        return tweepy.API(auth)

    def get_consumer_keys(self):
        """retrieve keys from engine and return in list as [consumer_key,consumer_secret]"""

        key=self.engine.get_attrib('consumer_key')
        secret=self.engine.get_attrib('consumer_secret')
        if key=='' or secret=='' or key==None or secret==None:
            self.state="waiting for consumer keys"
            self.engine.prompt_user("Visit the %s and create a twitter application with read and write permission" % (self.redirect_url), None)
            key=self.engine.prompt_user("Enter app key", str)
            secret=self.engine.prompt_user("Enter app secret", str)
            self.engine.set_attrib('consumer_key', key)
            self.engine.set_attrib('consumer_secret', secret)
        self.state="authenticating"
        return [key, secret]

    def get_user_keys(self):
        """retrieve keys from engine and return in list as [user_key,user_secret]"""

        token=self.engine.get_attrib('user_token')
        secret=self.engine.get_attrib('user_token_secret')
        if token=='' or secret=='' or token==None or secret==None:
            self.state="waiting for user keys"
##            self.redirect_url = self.auth.get_authorization_url()
            pin=self.engine.prompt_user("Visit the %s and enter the authorization pin" % (self.redirect_url), int)
            auth.get_access_token(pin)
            token=auth.access_token.key
            secret=auth.access_token.secret
            self.engine.set_attrib('user_token',token)
            self.engine.set_attrib('user_token_secret',secret)
        self.state="authenticating"
        return [token, secret]
