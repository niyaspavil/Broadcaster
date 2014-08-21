import plugin
import tweepy
import engine_mocker

class twitter(plugin.plugin):
    """plugin tweets msg to twitter"""
    
    def __init__(self,msg):
        """initialise and set message recieved for post"""
        self.msg=msg
        self.state="waiting"

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
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        user_token,user_token_secret=self.get_user_keys()
        auth.set_access_token(user_token, user_token_secret)
        return tweepy.API(auth)

##########################################################mocked####################################################################

    def get_consumer_keys(self):
        """retrieve keys from engine and return in list as [consumer_key,consumer_secret]"""
        engine=engine_mocker.Engine()
        key=engine.get_attrib('consumer_key')
        secret=engine.get_attrib('consumer_secret')
        if key=='' or secret=='':
            self.state="waiting for consumer keys"
            pass
        self.state="authenticating"
        return [key, secret]

    def get_user_keys(self):
        """retrieve keys from engine and return in list as [user_key,user_secret]"""
        engine=engine_mocker.Engine()
        token=engine.get_attrib('user_token')
        secret=engine.get_attrib('user_token_secret')
        if token=='' or secret=='':
            self.state="waiting for user keys"
            pass
        self.state="authenticating"
        return [token, secret]
###########################################################################################################################################
