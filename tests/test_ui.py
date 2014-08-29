
from ..Broadcaster import terminal_ui

import argparse

def test_main():

       terminal_ui.main(["hii", "-ch" ,"fb"]) 
	
       
def test_main_with_empty_message():

       terminal_ui.main([" ", "-ch","fb,twitter"])
def test_main_with_empty_channels():
       
       terminal_ui.main(["hello","-ch"," "])
def test_main():

       terminal_ui.main(["hello","-ch","fb", "twitter"])

