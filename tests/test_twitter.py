import random
import string
import engine_mocker
from Broadcaster import twitter

msg=''.join(random.choice(string.lowercase) for x in range(10))
tmp_plug=twitter.twitter(msg)
tmp_engine=tmp_plug.engine

def test_init():
    """test for twitter plugin initialisation"""

    assert tmp_plug.state=="waiting"
    assert tmp_plug.msg==msg

def test_status():
    """test for status method"""
    
    assert tmp_plug.status()=="waiting"

tmp_engine.mock_input="consumer999"

def test_get_consumer_keys():
    """test for get_consumer_keys method"""

    assert tmp_plug.get_consumer_keys()==['consumer999','consumer999']
    assert tmp_plug.get_consumer_keys()==['consumer999','consumer999']

tmp_engine.mock_input="user999"

def test_get_user_keys():
    """test for get_user_keys method"""

    assert tmp_plug.get_user_keys()==['user999','user999']
    assert tmp_plug.get_user_keys()==['user999','user999']

tmp_engine.conf={'consumer_key':'BCxhHxyTR4vHtKXqa7jSTicv4', 'consumer_secret':'sCpiNzjR9MTcFHbVWkuukm0ucKbYXnyv1ZdZQpDlRXAyzSMfpy', 'user_token':'2736495205-8f8yRTQeQ7JFhQHsqfSPWtl2iDafsJiiPsymOW1', 'user_token_secret':'vbzYBj1AbX4FZrrDtT2caQCVPt16Di0LTvsVArXTjQ3Ht'}

def test_post():
    """test for post method"""
    
    assert tmp_plugin.post()==True
