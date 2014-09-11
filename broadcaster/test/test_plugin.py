from ..plugin import Plugin
from .engine_mocker import Engine

engine=Engine("test")
class tester_plugin(Plugin):
    def __init__(self, engine, msg):
        pass
try:
    base_plugin=Plugin(engine, "failure")
except NotImplementedError:
    pass

plugin_test_obj=tester_plugin(engine, "error_test")

try:
    plugin_test_obj.post()
except NotImplementedError:
    pass

try:
    plugin_test_obj.status()
except NotImplementedError:
    pass

try:
    plugin_test_obj.force_exit()
except NotImplementedError:
    pass
