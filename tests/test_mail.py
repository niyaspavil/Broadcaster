import random
import string
import smtplib_mocker
from ..plugins import mail
from .engine_mocker import Engine
from ..Broadcaster.plugin import PluginError

msg=''.join(random.choice(string.lowercase) for x in range(10))
mail.smtplib = smtplib_mocker
mail.Engine= Engine
tmp_plug=mail.mail(msg)
tmp_engine=Engine("mail")
tmp_plug.engine=tmp_engine	
tmp_engine.mock_input="consumer999"


def test_init():
    """test for mail plugin initialisation"""

    assert tmp_plug.state=="waiting"
    assert tmp_plug.msg==msg

def test_status():
    """test for status method"""
    
    assert tmp_plug.status()=="waiting"

def test_get_consumer_details():
    """test for get_consumer_details method"""
  
    assert tmp_plug.get_consumer_details()==['consumer999','consumer999']
    assert tmp_plug.get_consumer_details()==['consumer999','consumer999']

def test_pre_authenicate():
    """test for pre_authenticate method"""
    assert tmp_plug.pre_authenticate()==True

def test_post():
    """test for post method"""
    tmp_plug.server = smtplib_mocker.SMTP() 
    assert tmp_plug.post()==True
