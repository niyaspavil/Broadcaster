
from .. import terminal_ui
from .raw_input_mocker import rawinput
import argparse
from .engine_mocker import broadcast,get_chnls

terminal_ui.broadcast = broadcast
terminal_ui.get_chnls = get_chnls
def test_main():

       terminal_ui.main(["-c=mail","hii"])       
def test_main_with_empty_message():
    try:
       terminal_ui.main([ "-c=mail"," ",])
       terminal_ui.main([ "-c=twitter"])
    except SystemExit:
	pass

def test_main_with_two_chanels():

       terminal_ui.main(["-c=mail,twitter",'message'])

def test_main_with_username():
       terminal_ui.main(["-c=mail:niyas,twitter:gorbin",'message'])
def test_prompt():
	terminal_ui.raw_input = rawinput
	tmp_ui=terminal_ui.Terminal_ui(["-c=mail,twitter","hello"],['mail','twitter'])
	tmp_ui.prompt("hello",None)
	tmp_ui.prompt("hello",str)
def test_ui_with_debug():
	
       terminal_ui.main(["-c=mail,twitter","hello","-dbug"])
def test_report_status():
	terminal_ui.report_status({'mail':'test'})

def test_reset_chanels():
       terminal_ui.main(["-rset","mail"])

def test_help():
      try:
          terminal_ui.main(["-h"])
      except SystemExit:
	pass

