
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
            args= parser.parse_args(args)
	except Exception:
		parser.print_help() 
        self.message =args.message
        self.channels = args.channels
	if args.debug:
	    self.debug=True
	else:
	    self.debug=False
    
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
            channel_list =self.channels[0].split(',') 
        else:
            channel_list=self.channels
        
        for i,item in enumerate(channel_list):        
            channel_list[i]=channel_list[i]

        channel_list = list(set(channel_list))   # removes duplicate channel names
        
        
        message= self.message                         
        

	if self.empty_message(message):  
	    self.display_error( "\t\tEnter valid message\t\t")
            return None

	elif self.empty_channel(channel_list):
            self.display_error("\t\tEnter any channel name\t\t")
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
    try:
        for i,optn in enumerate(args):
            if optn == '-rset' or optn == '--reset':
            	parser = argparse.ArgumentParser(
	            usage="\n\t -rset or --reset <channel name>\n",)
		parser.add_argument(
	        '-rset','--reset',type= str,nargs='+',choices=chnls,
	        help='used to reset user configuration of chanels..')
		arg= parser.parse_args(args)
                status=reset_plugin(arg.reset)
	        break
            else:
	        terminal_ui = Terminal_ui(args,chnls)  
    	        tup = terminal_ui.get_mesg_and_chanl()
    	        if tup:
                    status=broadcast(tup[0],tup[1],tup[2],terminal_ui)
		break
    except Exception as e:
        print e
    if status:
    	report_status(status)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
