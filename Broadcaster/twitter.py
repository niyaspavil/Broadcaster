import plugin
import tweepy
import engine_mocker

class Tweet(plugin.Plugin):
    """plugin tweets msg to twitter"""
    
    def __init__(self,msg):
        """initialise and set message recieved for post"""
        self.msg=msg

    def post(self):
        """Method to invoke plugin to post message to site"""
        consumer_key,consumer_secret=get_consumer_keys()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        user_token,user_token_secret=get_user_keys()
        auth.set_access_token(user_token, user_token_secret)
        api = tweepy.API(auth)
        api.update_status(self.msg)
        return True

    def status(self):
        """Method to query status of the plugin activity"""
        raise NotImplementedError()

    def force_exit(self):
        """This method should kill the plugin activity"""
        raise NotImplementedError()

##########################################################mocked####################################################################
 
def get_consumer_keys():
    """retrieve keys from engine and return in list as [consumer_key,consumer_secret]"""
    mocker=engine_mocker.Engine()
    return [mocker.get_attrib('consumer_key'), mocker.get_attrib('consumer_secret')]

def get_user_keys():
    """retrieve keys from engine and return in list as [user_key,user_secret]"""
    mocker=engine_mocker.Engine()
    return [mocker.get_attrib('user_token'), mocker.get_attrib('user_token_secret')]
