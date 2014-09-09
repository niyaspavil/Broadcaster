from ..Broadcaster import dummy_engine
from ..tests.plugin_mocker import plugin_mocker
from ..tests.mock_ui import Mock_ui
import os
import shutil

UI=Mock_ui()
dummy_engine.cfgfile="/tmp/test/conf.ini"
dummy_engine.plugins_dir="./plugins"

def test_engine():
    dummy_engine.cfgfile="/tmp/test/conf.ini"
    dummy_engine.private_home="/tmp/test"
    engine=dummy_engine.Engine("test_section")
    engine.UI=UI
    assert engine.get_attrib("twitter") == ""
    engine.set_attrib("user","999")
    assert engine.get_attrib("user") == "999"
    engine.prompt_user("hello",str)
    shutil.rmtree("/tmp/test")

def test_load_plugin():
    dummy_engine.load_plugin("twitter","test")

def test_broadcast():
    dummy_engine.load_plugin=plugin_mocker
    assert dummy_engine.broadcast("testing", ['twitter'], False, UI) == {"twitter":"Successful"}
    dummy_engine.load_plugin=fail_post
    assert dummy_engine.broadcast("testing", ['twitter'], False, UI) == {"twitter":"Failed"}

def fail_post(chn, msg):
    pass

def test_get_chnls():
    dummy_engine.get_chnls()
