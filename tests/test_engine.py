from ..Broadcaster import dummy_engine
from ..tests.plugin_mocker import plugin_mocker
from ..tests.mock_ui import Mock_ui

load_plugin=dummy_engine.load_plugin

def test_broadcast():
    ui=Mock_ui()
    dummy_engine.load_plugin=plugin_mocker
    dummy_engine.broadcast("testing", ['twitter'],ui)

def test_load_plugin():
    load_plugin("twitter","test",)
