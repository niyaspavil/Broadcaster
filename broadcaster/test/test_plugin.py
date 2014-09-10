from ..plugin import Plugin

class tester_plugin(Plugin):
    def __init__(self, msg):
        pass
try:
    base_plugin=Plugin("failure")
except NotImplementedError:
    pass

plugin_test_obj=tester_plugin("error_test")

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
