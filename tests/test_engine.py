from ..Broadcaster.dummy_engine import Engine 
from ..tests.plugin_mocker import plugin_mocker
from ..tests.mock_ui import Mock_ui

UI=Mock_ui()
cfgfile="/tmp/conf.ini"

def test_engine():
    engine=dummy_engine.Engine()
    engine.UI=UI
    engine.get_attrib("twitter")
    engine.set_attrib("user","999")
    engine.get_attrib("user")
    engine.prompt_user("hello",str)

from ..Broadcaster import dummy_engine

load_plugin=dummy_engine.load_plugin

def test_broadcast():
    dummy_engine.load_plugin=plugin_mocker
    dummy_engine.broadcast("testing", ['twitter'],UI)

def test_load_plugin():
    load_plugin("twitter","test")



