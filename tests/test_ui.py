from Broadcaster import terminal_ui


temp_ui =terminal_ui.Terminal_ui()

def test_init():

	assert temp_ui.message == "message"
	assert temp_ui.channels == ['fb,twitter']

def test_get_msg():
	
	assert temp_ui.get_mesg_and_chanl() == ("message",['fb','twitter'])
                   
