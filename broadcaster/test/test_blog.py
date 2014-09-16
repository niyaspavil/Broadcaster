import random
import string
import xmlrpc_mocker
from ..plugins import blog
from .engine_mocker import Engine
from ..plugin import PluginError

msg=''.join(random.choice(string.lowercase) for x in range(random.choice (range(1,20))))
blog.xmlrpc = xmlrpc_mocker
engine=Engine("blog")
tmp_plug=blog.blog(engine, msg)
tmp_plug.engine.mock_input="consumer999"

def test_init():
    assert tmp_plug.state=="waiting"
    assert tmp_plug.msg==msg

def test_pre_authenticate():
    assert tmp_plug.pre_authenticate() == True
    
def test_customer_details():
    assert tmp_plug.customer_details() == ["vinayak","password"]

def test_compose_post():
    assert post = {
        'title': '',
        'description': self.msg,
        'categories': '',
        'dateCreated': "todays date",
        'mt_keywords': ''
    }
    
def test_post():
    assert tmp_plug.post() == True

