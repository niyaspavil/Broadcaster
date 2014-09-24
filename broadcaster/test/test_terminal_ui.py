from.. import engine
from .. import terminal_ui
from .raw_input_mocker import rawinput
from . getpass_mocker import getpass
import argparse
from .engine_mocker import broadcast,get_chnls,reset_channels

terminal_ui.broadcast = broadcast
terminal_ui.get_chnls = get_chnls
terminal_ui.reset_channels = reset_channels
def test_main():

       terminal_ui.main(["-ch=mail","hii"])       
def test_main_with_empty_message():
    try:
       terminal_ui.main([ "-ch=mail"," ",])
       terminal_ui.main([ "-ch=twitter"])
    except SystemExit:
	pass

def test_main_with_two_chanels():

       terminal_ui.main(["-ch=mail,twitter",'message'])

def test_main_with_username():
       terminal_ui.main(["-ch=mail:niyas,twitter:gorbin",'message'])

def test_prompt():
	terminal_ui.getpass.getpass = getpass
	terminal_ui.raw_input = rawinput
	tmp_ui=terminal_ui.Terminal_ui(["-ch=mail,twitter","hello"],['mail','twitter'])
	tmp_ui.prompt("hello",engine.INPUT_TYPE_NONE)
	tmp_ui.prompt("hello",engine.INPUT_TYPE_NUMBER)
	tmp_ui.prompt("hello",engine.INPUT_TYPE_TEXT_ONELINE)
	tmp_ui.prompt("hello",engine.INPUT_TYPE_TEXT_PASSWORD)
	try:
	    tmp_ui.prompt("hello",engine.INPUT_TYPE_TEXT_MULTILINE)
	except IOError:
	    pass
def test_ui_with_debug():
	
       terminal_ui.main(["-ch=mail,twitter","hello","-dbug"])

def test_report_status():
	terminal_ui.report_status({'mail':'test'})

def test_reset_chanels():
        terminal_ui.main(["-rset","mail"])
	terminal_ui.main(["-rset","mail:user"])      

def test_help():
      try:
          terminal_ui.main(["-h"])
      except SystemExit:
	pass
