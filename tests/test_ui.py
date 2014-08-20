
from Broadcaster import Ui
from Broadcaster import Mock_engin


test =Ui.Terminal_Ui()
f=test.get_message_and_channel()
if f:
    k=Mock_engin.engin(f)

    print k.get_response()
