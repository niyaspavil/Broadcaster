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

