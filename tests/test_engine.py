from ..Broadcaster import dummy_engine
from ..tests.plugin_mocker import plugin_mocker


load_plugin=dummy_engine.load_plugin

def test_broadcast():
    dummy_engine.load_plugin=plugin_mocker
    dummy_engine.broadcast("testing", ['twitter'])

def test_load_plugin():
    load_plugin("twitter","test")
