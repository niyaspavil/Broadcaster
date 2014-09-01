
from ui import *
from dummy_engine import broadcast
import argparse
from termcolor import colored
class Terminal_ui(Ui):
    
    def __init__(self,args):    
        """
                     This constructor  read user input from the terminal.
                     
        """
        parser = argparse.ArgumentParser(usage='%(prog)s <your message> -ch <channel_list>',description='A way for Broadcast your messages')
        parser.add_argument('message',type=str, help='Message to be sended')
        parser.add_argument( '-ch', '--channels',type= str,nargs='+', required=True,help='Channel list to send the message',)
        args= parser.parse_args(args)
        self.message =args.message
        self.channels = args.channels
    
    def empty_message (self,Message):
       
        """
                                  check message is empty or not
        """
	if not Message.strip():
            return True
 	else:
  		return False
           
        
    def empty_channel(self,Channel_List):
        """
                                    check channels are empty or not
        """
        if not Channel_List[0].strip():
              return True
        else:
              return False
        
    
    def get_mesg_and_chanl(self):
        
        """
               This Function separate message and channel list from user input.
        """
        
        if len(self.channels) == 1:     
            channel_list =self.channels[0].split(',')   # removes ',' and split into list
        else:
            channel_list=self.channels
        
        for i,item in enumerate(channel_list):        # removes space in channels list
            channel_list[i]=channel_list[i]

        channel_list = list(set(channel_list))         # removes duplicate channel names
        
        
        message= self.message                          # message contains message to be sended
        

	if self.empty_message(message):  # check the message is empty or not
		self.display_error( "\t\tEnter valid message\t\t")
                return None

	elif self.empty_channel(channel_list):
                self.display_error("\t\tEnter any channel name\t\t")
                return None
        else:
            return (message,channel_list)  
                 
    def display_error(self,error):
        
        """
                  This Function displays the  errors
        """
   
        print colored("Error",'red')
    	print colored(error,'red')
        print"\n"*7
    def prompt(self,content):

	"""

		     This abstract function will prompt some content to the user and return reply to the engine
	"""


	return raw_input(colored(content+":\n >>>\t",'red'))
	
	




def report_status(status):
	
	for channel,statu in status.items():
		print channel+">>>"+statu	
    

def main(args):
    status= None
    terminal_ui = Terminal_ui(args)
    tup = terminal_ui.get_mesg_and_chanl()
    if tup:
        status=broadcast(tup[0],tup[1],terminal_ui)
    if status:
    	report_status(status)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
