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

def is_None_Or_Empty_Or_BlankString (myString):
       
        """
                    This Function is used to check message is empty or not. Return 'True' when empty message comes
        """
	if myString:
  		if not myString.strip():
   			return True
 	else:
  		return True

 	return False     
           

class Terminal_Ui(Ui):
    
    def __init__(self):
        
        """
                     This Function  read user input from the terminal.
                     Format for user input is <message> -ch <channel list> or <message> --channels <channel list>
                           for example: Hello -ch fb,twitter
        """

        parser = argparse.ArgumentParser(usage='%(prog)s <your message> -ch <channel_list>',description='A way for Broadcast your messages')

        parser.add_argument('message',type=str, help='Message to be sended')
        parser.add_argument( '-ch', '--channels',type= str, required=True,help='Channel list to send the message',)
        args= parser.parse_args()
        self.message =args.message
        self.channels = args.channels

    
        
        
        
    
    def get_message_and_channel(self):
        
        """
               This Function separate message and channel list from user input. Return a tuple of message string and list of channels 
                 For example: heloo -ch fb,gmail ----->>>>>> ("heloo",['fb,gmail'])
        """
        print self.channels
        channel_list=self.channels.split(',')
	message= self.message

	if  is_None_Or_Empty_Or_BlankString(message):
		print "\n\n\nEnter valid message\n\n\n"
	elif not channel_list:
                print "\n\n\nEnter any channel name\n\n\n"
	else:
            
        	return (message,list(set(channel_list)))
                 
    def display_status_and_error(self):
        
        "display the status and error return from other levels"

        pass
   
