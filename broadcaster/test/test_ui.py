from ..ui import Ui

class tester_ui(Ui):
    def __init__(self):
        pass
try:
    base_ui=Ui()
except NotImplementedError:
    pass

ui_test_obj=tester_ui()

try:
    ui_test_obj.get_mesg_and_chanl()
except NotImplementedError:
    pass

try:
    ui_test_obj.display_error("test error")
except NotImplementedError:
    pass

try:
    ui_test_obj.prompt("test prompt")
except NotImplementedError:
    pass
