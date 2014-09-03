import random
import string
import smtplib_mocker
from ..plugins import mail
from .engine_mocker import Engine
from ..Broadcaster.plugin import PluginError

msg=''.join(random.choice(string.lowercase) for x in range(10))
tmp_plug=mail.mail(msg)
tmp_engine=Engine("mail")
tmp_plug.engine=tmp_engine
tmp_plug.smtplib=smtplib_mocker
tmp_engine.mock_input="consumer999"



try:
    test_msg=''.join(random.choice(string.lowercase) for x in range(200))
    mail.mail(test_msg)
except PluginError:
    pass

def test_init():
    """test for twitter plugin initialisation"""

    assert tmp_plug.state=="waiting"
    assert tmp_plug.msg==msg

def test_status():
    """test for status method"""
    
    assert tmp_plug.status()=="waiting"

def test_get_consumer_details():
    """test for get_consumer_keys method"""

    assert tmp_plug.get_consumer_details()==['consumer999','consumer999']
    assert tmp_plug.get_consumer_details()==['consumer999','consumer999']

def test_compose_mail():
    """test for get_user_keys method"""

    tmp_plug.auth=tweepy_mocker.OAuthHandler()
    assert tmp_plug.get_user_keys()==['user999','user999']
    assert tmp_plug.get_user_keys()==['user999','user999']

def test_post():
    """test for post method"""
    
    assert tmp_plug.post()==True

#def test_real():
#    tmp_plug=twitter.twitter(msg)
#    assert tmp_plug.post()==True
