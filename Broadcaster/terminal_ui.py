
from ui import *
from dummy_engine import broadcast,get_chnls,reset_plugin
import argparse
from termcolor import colored
class Terminal_ui(Ui):
    
    def __init__(self,args,chnls):    
        """
            This constructor  read user input from the terminal.
                     
        """
	try:
	    self.reset = False
	    self.message = False
	    self.channels = False
	    self.debug = False
            parser = argparse.ArgumentParser(
	        usage="\n\t%(prog)s <your message> -ch <channel_list> [-dbug]\n",
	        description='A way for Broadcast your messages')
            parser.add_argument(
	        'message',type=str, help='Message to be sended')
            parser.add_argument( 
                '-ch', '--channels',type= str,nargs='+',
	        choices=chnls,required=True,help='Channel list to send the message')
	    parser.add_argument(
	        '-dbug','--debug',action='store_true',
	        help='give more useful and informative output to understand error..')
	    parser_reset = argparse.ArgumentParser(
	            usage="\n\t -rset or --reset <channel name>\n",)
	    parser_reset.add_argument(
	        '-rset','--reset',type= str,nargs='+',choices=chnls,
	        help='used to reset user configuration of chanels..')
	    print args
	    if ('-rset' or '--reset') in args:
		
	        arg= parser_reset.parse_args(args)
		self.reset = arg.reset
		
	    else:
            	args= parser.parse_args(args)
		self.message = args.message
		self.channels = args.channels
		self.debug = args.debug	
	except Exception as e:
		#parser.print_help() 
		print e	

    
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
   
        print colored("Error",'red')
    	print colored(error,'red')
        print"\n"*7
    
    def prompt(self,content,type):

	"""
              Function for prompt some datas to user
	"""
	if(type == None):
	
		print colored(content+":\n >>>\t",'green')
	else:
	    return raw_input(colored(content+":\n >>>\t",'green'))
	
	




def report_status(status):
	
	for channel,statu in status.items():
	    print channel+">>>"+statu	
    

def main(args):
    status= None
    chnls=get_chnls()
    terminal_ui = Terminal_ui(args,chnls)
    if terminal_ui.reset:
	status = reset_plugin(terminal_ui.reset)
    else:  
        tup = terminal_ui.get_mesg_and_chanl()
    	if tup:
            status=broadcast(tup[0],tup[1],tup[2],terminal_ui)
    if status:
    	report_status(status)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
