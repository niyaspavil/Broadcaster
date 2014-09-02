from ..Broadcaster.dummy_engine import Engine 
from ..tests.plugin_mocker import plugin_mocker
from ..tests.mock_ui import Mock_ui
import os

UI=Mock_ui()

def test_engine():
    
    engine=dummy_engine.Engine("test_section")
    engine.UI=UI
    engine.get_attrib("twitter")
    engine.set_attrib("user","999")
    engine.get_attrib("user")
    engine.prompt_user("hello",str)

from ..Broadcaster import dummy_engine

def test_load_plugin():
    dummy_engine.load_plugin("twitter","test")

def test_broadcast():
    dummy_engine.load_plugin=plugin_mocker
    dummy_engine.broadcast("testing", ['twitter'],UI)
    dummy_engine.load_plugin=fail_post
    dummy_engine.broadcast("testing", ['twitter'],UI)

def fail_post(chn, msg):
    pass
