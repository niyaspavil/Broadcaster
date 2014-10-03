from .. import engine
from .plugin_mocker import plugin_mocker
from .mock_ui import Mock_ui
import os
import shutil
import ConfigParser

UI=engine.__ui__=Mock_ui()
engine.__cfgfile__="/tmp/test/conf.ini"
engine.__plugins_dir__="./broadcaster/plugins"

def test_engine():
    engine.__cfgfile__="/tmp/test/conf.ini"
    engine.__private_home__="/tmp/test"
    tmp_conf=engine.get_conf()
    temp_engine=engine.Engine("test_section:user")
    engine.__conf__=tmp_conf
    assert temp_engine.get_attrib("user") == ""
    temp_engine.set_attrib("user","999")
    engine.set_conf(engine.__conf__)
    assert temp_engine.get_attrib("user") == "999"
    assert engine.reset_channels([("test_section","user")])=={"test_section:user":"reset success"}
    temp_engine.prompt_user("hello",str)
    shutil.rmtree("/tmp/test")

def test_load_plugin():
    engine.load_plugin("twitter", "user", "test")
    engine.load_plugin("twitter", "", "test")

def test_broadcast():
    engine.load_plugin=plugin_mocker
    assert engine.broadcast("testing", [('twitter','user')], False, UI) == {"twitter:user":"Successful"}
    engine.load_plugin=fail_post
    assert engine.broadcast("testing", [('twitter', 'user')], False, UI) == {"twitter:user":"Failed ::-> 'NoneType' object has no attribute 'post'"}

def fail_post(chn, user, msg):
    pass

def test_get_chnls():
    engine.get_channels()
