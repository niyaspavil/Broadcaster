import argparse

class Ui(object):

    def __init__(self):
    
        """
                     This is a abstract Function for read user input
        """
        
        raise NotImplementedError
    
    def get_message_and_channel(self):
        
        """
                     This is a abstract Function for get message and channel list from user input
        """

        raise NotImplementedError
    
    def display_status_and_error(self):
        
        """
                     This is a abstract Function for display the status and error return from other levels
        """
        raise NotImplementedError



class Terminal_Ui(Ui):
    
    def __init__(self):
        
        """
                     This Function  read user input from the terminal.
                     Format for user input is <message> -ch <channel list> or <message> --channels <channel list>
                           for example: Hello -ch fb,twitter
        """

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
	if myString:
  		if not myString.strip():
   			return True
 	else:
  		return True

 	return False     
           
        
    def is_empty_list(self,myList):
        """
               This Function check channel is empty or not
        """
        if myList == [' ']:
              return True
        else:
              return False
        
    
    def get_message_and_channel(self):
        
        """
               This Function separate message and channel list from user input. Return a tuple of message string and list of channels 
                 For example: heloo -ch fb,gmail ----->>>>>> ("heloo",['fb,gmail'])
        """
        
        if len(self.channels) == 1:
            channel_list =self.channels[0].split(',')  # channel_list contains channel names inputed  
        else:
            channel_list=self.channels
        print channel_list
        for i,item in enumerate(channel_list):
            channel_list[i]=channel_list[i]

        channel_list = list(set(channel_list))         # removes duplicate channel names
        
        
        message= self.message                          # message contains message to be sended
        

	if self.is_None_Or_Empty_Or_BlankString(message):  # check the message is empty or not
		print "\n\n\nEnter valid message\n\n\n"
	elif self.is_empty_list(channel_list):
                print "\n\n\nEnter any channel name\n\n\n"
	else:
            
        	return (message,channel_list)  
                 
    def display_status_and_error(self):
        
        "display the status and error return from other levels"

        pass
   
