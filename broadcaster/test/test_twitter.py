import random
import string
import tweepy_mocker
from ..plugins import twitter
from .engine_mocker import Engine
from ..plugin import PluginError

msg=''.join(random.choice(string.lowercase) for x in range(10))
twitter.tweepy=tweepy_mocker
twitter.Engine=Engine
tmp_plug=twitter.twitter(msg)
tmp_plug.engine.mock_input="consumer999"

try:
    test_msg=''.join(random.choice(string.lowercase) for x in range(200))
    twitter.twitter(test_msg)
except PluginError:
    pass

def test_init():
    """test for twitter plugin initialisation"""

    assert tmp_plug.state=="waiting"
    assert tmp_plug.msg==msg

def test_status():
    """test for status method"""
    
    assert tmp_plug.status()=="waiting"

def test_get_consumer_keys():
    """test for get_consumer_keys method"""

    assert tmp_plug.get_consumer_keys()==['consumer999','consumer999']
    assert tmp_plug.get_consumer_keys()==['consumer999','consumer999']

def test_get_user_keys():
    """test for get_user_keys method"""

    tmp_plug.auth=tweepy_mocker.OAuthHandler("consumer999", "consumer999")
    
    assert tmp_plug.get_user_keys()==['user999','user999']
    assert tmp_plug.get_user_keys()==['user999','user999']

def test_post():
    """test for post method"""
    assert tmp_plug.post()==True

def test_exception():
    tmp_plug.engine=Engine("twitter")
    tmp_plug.engine.mock_input="consumer9999"
    tmp_plug.auth.access_token.key=""
    try:
        tmp_plug.post()
    except PluginError:
        pass
    tmp_plug.engine.conf={"consumer_key":"consumer999", "consumer_secret":"consumer999","user_token":"kjkl","user_token_secret":"fg"}
    try:
        tmp_plug.post()
    except PluginError:
        pass
    twitter.Engine="fake_engine"
    try:
        plug=twitter.twitter(msg)
    except PluginError:
        pass

#def test_real():
#    tmp_plug=twitter.twitter(msg)
#    assert tmp_plug.post()==True
