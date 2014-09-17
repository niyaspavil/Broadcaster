
from .. import terminal_ui
from .raw_input_mocker import rawinput
import argparse
from .engine_mocker import broadcast,get_chnls

terminal_ui.broadcast = broadcast
terminal_ui.get_chnls = get_chnls
def test_main():

       terminal_ui.main(["hii","-c","mail"]) 
       
def test_main_with_empty_message():

       terminal_ui.main([" ", "-c","mail","twitter"])
def test_main_with_two_chanels():

       terminal_ui.main(["hello","-c","mail", "twitter"])
def test_prompt():
	terminal_ui.raw_input = rawinput
	tmp_ui=terminal_ui.Terminal_ui(["hello","-c","mail", "twitter"],['mail','twitter'])
	tmp_ui.prompt("hello",None)
	tmp_ui.prompt("hello",str)
def test_ui_with_debug():
	
       terminal_ui.main(["hello","-c","mail", "twitter","-dbug"])
def test_report_status():
	terminal_ui.report_status({'mail':'test'})

def test_reset_chanels():
       terminal_ui.main(["-rset","mail"])

def test_help():
      try:
          terminal_ui.main(["-h"])
      except SystemExit:
	pass


