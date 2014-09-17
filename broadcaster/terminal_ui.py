from ui import *
from engine import broadcast,get_channels,reset_channels
import argparse
from termcolor import colored
import sys
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
	    'message',type=str, help=colored('Message to be sended','cyan'))
        parser.add_argument( 
            '-c', '--channels',type= str,nargs='+',default=chnls,
	    choices=chnls,help=colored('Channel list to send the message','cyan'))
	parser.add_argument(
	    '-dbug','--debug',action='store_true',
	    help=colored('give more useful and informative output to understand error..','cyan'))
	   
	parser_reset = argparse.ArgumentParser(
	    usage=colored("\n\t -rset or --reset <channel name>\n",'yellow',attrs=['bold']))
	parser_reset.add_argument(
	    '-rset','--reset',type= str,nargs='+',choices=chnls,
	    help=colored('used to reset user configuration of chanels..','cyan'))
	if '-rset' in args or '--reset' in args:
	    arg= parser_reset.parse_args(args)
	    self.reset = arg.reset
	elif '-h' in args or '--help' in args:
	    print ""
	    sys.exit()  	
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
        channel_list = list(set(self.channels))   # removes duplicate channel names
        message= self.message                         
        if self.empty_message(message):  
	    self.display_error( "\t\tEnter valid message\t\t")
            return None
        else:
            return (message,channel_list,self.debug)  
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
	if(type == None):
	    print colored('\n'+content+"\n",'green')
	else:
	    return raw_input(colored('\n'+content+":\n >>>\t",'green'))

def report_status(status):
    for channel,stats in status.items():
        print colored(channel+">>>"+stats,'green')	
    

def main(args):
    status= None
    chnls=get_channels()        # recieves plugin names from engine
    terminal_ui = Terminal_ui(args,chnls)
    if terminal_ui.reset:
	status = reset_channels(terminal_ui.reset)
    else:  
        tup = terminal_ui.get_mesg_and_chanl()
    	if tup:
            status=broadcast(tup[0],tup[1],tup[2],terminal_ui) #return channel,message,debug-mode and ui object to engine
    if status:
    	report_status(status)
