from .. import engine
from .plugin_mocker import plugin_mocker
from .mock_ui import Mock_ui
import os
import shutil
import ConfigParser

UI=Mock_ui()
engine.__cfgfile__="/tmp/test/conf.ini"
engine.__plugins_dir__="./broadcaster/plugins"

def test_engine():
    engine.__cfgfile__="/tmp/test/conf.ini"
    engine.__private_home__="/tmp/test"
    tmp_conf=engine.get_conf()
    engin=engine.Engine("test_section")
    engin.UI=UI
    engine.__conf__=tmp_conf
    assert engin.get_attrib("twitter") == ""
    engin.set_attrib("user","999")
    engine.set_conf(engine.__conf__)
    assert engin.get_attrib("user") == "999"
    assert engine.reset_channels(["test_section"])=={"test_section":"reset"}
    engin.prompt_user("hello",str)
    shutil.rmtree("/tmp/test")

def test_load_plugin():
    engine.load_plugin("twitter", "user", "test")

def test_broadcast():
    engine.load_plugin=plugin_mocker
    assert engine.broadcast("testing", [('twitter','user')], False, UI) == {"twitter":"Successful"}
    engine.load_plugin=fail_post
    assert engine.broadcast("testing", [('twitter', 'user')], False, UI) == {"twitter":"Failed ::-> 'NoneType' object has no attribute 'post'"}

def fail_post(chn, user, msg):
    pass

def test_get_chnls():
    engine.get_channels()
