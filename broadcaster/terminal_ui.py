from ui import *
from engine import broadcast,get_channels,reset_channels
import engine
import argparse
from termcolor import colored
import sys
import getpass
class Terminal_ui(Ui):
    
    def __init__(self,args,chnls):    
        """
            This constructor  read user input from the terminal.
                     
        """
	self.reset = False
	self.message = False
	self.channels = False
	self.debug = False
        parser = argparse.ArgumentParser(
	    usage=colored(
              "\n\tEnter 'your message' -ch <channel list> [-dbug]"+'\n \t\t\tor\n'
	      +"\tEnter -rset or --reset <channel list>"+'\n \t\t\tor\n'
	      +"\tEnter -h or --help for more help",'yellow',attrs=[ 'bold']),
	      description=colored('A way for Broadcast your messages','magenta',attrs=[ 'bold']))
        parser.add_argument( 
            '-ch','--channels',type= str,nargs='+',default=chnls,
	    help=colored('Channel list to send the message','cyan'))
	parser.add_argument(
	    'message',type=str, help=colored('Message to be sended','cyan'))
	parser.add_argument(
	    '-dbug','--debug',action='store_true',
	    help=colored('give more useful and informative output to understand error..','cyan'))
	   
	parser_reset = argparse.ArgumentParser(
	    usage=colored("\n\t -rset or --reset <channel name>\n",'yellow',attrs=['bold']))
	parser_reset.add_argument(
	    '-rset','--reset',type= str,nargs='+',
	    help=colored('used to reset user configuration of chanels..','cyan'))
	if '-rset' in args or '--reset' in args:
	    arg= parser_reset.parse_args(args)
	    self.reset = arg.reset 	
	else:
            args= parser.parse_args(args)
	    self.message = args.message
	    self.channels = args.channels
	    self.debug = args.debug
    def empty_message (self,Message):
       
        """
                       check message is empty or not
        """
	if not Message.strip():
            return True
 	else:
  	    return False
           
    def get_mesg_and_chanl(self):
        
        """
               This Function separate message and channel list from user input.
        """
	self.channels = self.channels[0].split(',')
        channel_list = list(set(self.channels))    # removes duplicate channel names
	channels=[]
	for i in channel_list:
	    if i.find(":")==-1:
		i=i+":"
	    channels.append(tuple(i.split(':')))
	message= self.message                         
        if self.empty_message(message):  
	    self.display_error( "\t\tEnter valid message\t\t")
            return None
        else:
            return (message,channels,self.debug)  
    def display_error(self,error):
        
        """
                  This Function displays the  errors
        """
        print colored("\nError"+'\t>>>'+error,'red')
        print"\n"*7
    def prompt(self,content,type):

	"""
              Function for prompt some datas to user
	"""
	if(type == engine.INPUT_TYPE_NONE):
	    print colored('\n'+content+"\n",'green')
	elif(type == engine.INPUT_TYPE_NUMBER):
	    return raw_input(colored('\n'+content+":\n >>>\t",'green'))
	elif(type == engine.INPUT_TYPE_TEXT_ONELINE):
	    return raw_input(colored('\n'+content+":\n >>>\t",'green'))
	elif(type == engine.INPUT_TYPE_TEXT_PASSWORD):
	    return getpass.getpass(colored('\n'+content+":\n >>>\t",'green'))
	else:
	    print colored('\n'+content+"\n Enter Ctrl+d for exit\n",'green')
	    return sys.stdin.read()
	
	
def report_status(status):
    for channel,stats in status.items():
        print colored(channel+">>>"+stats,'green')	
    

def main(args):
    status= None
    reset=[]
    chnls=get_channels()        # recieves plugin names from engine
    terminal_ui = Terminal_ui(args,chnls)
    if terminal_ui.reset:
	for i in terminal_ui.reset:
	    if i.find(":")==-1:
		i=i+":"
	    reset.append(tuple(i.split(':')))
	status = reset_channels(reset)
    else:  
        tup = terminal_ui.get_mesg_and_chanl()
    	if tup:
            status=broadcast(tup[0],tup[1],tup[2],terminal_ui) #return channel,message,debug-mode and ui object to engine
    if status:
    	report_status(status)
