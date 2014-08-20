import argparse

class Ui(object):

    def __init__(self):
    
        """
                     This is a constructor for read user input
        """
        
        raise NotImplementedError
    
    def get_message_and_channel(self):
        
        """
                     This is a abstract Function for get message and channel list from user input
        """

        raise NotImplementedError
    
    def display_status(self):
        
        """
                     This is an abstract Function for display the status return from other levels
        """
        raise NotImplementedError
    
    def display_error(self):
        
        """
                     This is an abstract function for display the error 
        """

class Terminal_Ui(Ui):
    
    def __init__(self):
        
        """
                     This constructor  read user input from the terminal.
                     Format for user input is <message> -ch <channel list> or <message> --channels <channel list>
                           for example: Hello -ch fb,twitter
        """
        print"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""
        parser = argparse.ArgumentParser(usage='%(prog)s <your message> -ch <channel_list>',description='A way for Broadcast your messages')

        parser.add_argument('message',type=str, help='Message to be sended')
        parser.add_argument( '-ch', '--channels',type= str,nargs='+', required=True,help='Channel list to send the message',)
        args= parser.parse_args()
        self.message =args.message
        self.channels = args.channels

    
    def is_None_Or_Empty_Or_BlankString (self,myString):
       
        """
                    This Function is used to check message is empty or not. Return 'True' when empty message comes
        """
	if not myString.strip():
            return True
 	else:
  		return False
           
        
    def is_empty_list(self,myList):
        """
               This Function check channel is empty or not
        """
        if not myList[0].strip():
              return True
        else:
              return False
        
    
    def get_message_and_channel(self):
        
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
        

	if self.is_None_Or_Empty_Or_BlankString(message):  # check the message is empty or not
		self.display_error( "\t\tEnter valid message\t\t")
	elif self.is_empty_list(channel_list):
                self.display_error("\t\tEnter any channel name\t\t")
	else:
            
        	return (message,channel_list)  
                 
    def display_error(self,error):
        
        "display the  error"

        print"                                                           ----------ERROR---------    "
        print error
