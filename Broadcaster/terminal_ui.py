from .ui import *
import argparse


class Terminal_ui(Ui):
    
    def __init__(self,args):
        
        """
                     This constructor  read user input from the terminal.
                     
        """
       # arg= " message -ch fb,twitter"
        parser = argparse.ArgumentParser(usage='%(prog)s <your message> -ch <channel_list>',description='A way for Broadcast your messages')
	self.message=None
	self.channels=[]
        parser.add_argument('message',type=str, help='Message to be sended')
        parser.add_argument( '-ch', '--channels',type= str,nargs='+', required=True,help='Channel list to send the message',)
        args= parser.parse_args(args)
        self.message =args.message
        self.channels = args.channels
    
    def empty_message (self,Message):
       
        """
                    This Function is used to check message is empty or not. Return 'True' when empty message comes
        """
	if not Message.strip():
            return True
 	else:
  		return False
           
        
    def empty_channel(self,Channel_List):
        """
               This Function check channel is empty or not
        """
        if not Channel_List[0].strip():
              return True
        else:
              return False
        
    
    def get_mesg_and_chanl(self):
        
        """
               This Function separate message and channel list from user input. Return a tuple of message string and list of channels 
                 For example: heloo -ch fb,gmail ----->>>>>> ("heloo",['fb,gmail'])
        """
        
        if len(self.channels) == 1:         # channel_list contains channel names inpute
            channel_list =self.channels[0].split(',')   # removes ',' and split into list
        else:
            channel_list=self.channels
        
        for i,item in enumerate(channel_list):        # removes space in channels list
            channel_list[i]=channel_list[i]

        channel_list = list(set(channel_list))         # removes duplicate channel names
        
        
        message= self.message                          # message contains message to be sended
        

	if self.empty_message(message):  # check the message is empty or not
		self.display_error( "\t\tEnter valid message\t\t")

	elif self.empty_channel(channel_list):
                self.display_error("\t\tEnter any channel name\t\t")
	
        else:
            return (message,channel_list)  
                 
    def display_error(self,error):
        
        """
                  This Function displays the  errors
        """

        print"\n                                                            ----------ERROR---------    "
 
        print"""\n\n\n%*100\n\n\n\n"""


def main(args):
    terminal_ui = Terminal_ui(args)
    tup = terminal_ui.get_mesg_and_chanl()
    return tup

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
