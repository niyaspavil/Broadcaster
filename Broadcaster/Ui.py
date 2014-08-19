import argparse

class Ui(object):

    def __init__(self):
    
        "read user input"
        
        raise NotImplementedError
    
    def get_message_and_channel(self):
        
        "separate message and channel list from user input"

        raise NotImplementedError
    
    def display_status_and_error(self):
        
        "display the status and error return from other levels"
        raise NotImplementedError
def is_None_Or_Empty_Or_BlankString (myString):
 if myString:
  if not myString.strip():
   return True
 else:
  return True

 return False     
           

class Terminal_Ui(Ui):
    
    def __init__(self):
        
        "read user input from the terminal"

        parser = argparse.ArgumentParser(usage='%(prog)s <your message> -ch <channel_list>',description='A way for Broadcast your messages')

        parser.add_argument('message',type=str, help='Message to be sended')
        parser.add_argument( '-ch', '--channels',type= str, required=True,help='Channel list to send the message',)
        args= parser.parse_args()
        self.message =args.message
        self.channels = args.channels

    
        
        
        
    
    def get_message_and_channel(self):
        
        "separate message and channel list from user input"
        channel_list=self.channels.split()
	msg= self.message

	if  is_None_Or_Empty_Or_BlankString(msg):
		print "enter valid message"
	elif not channel_list:
			print "Enter any channel name"
	else:
        	return (self.message,channel_list)
    
    def display_status_and_error(self):
        
        "display the status and error return from other levels"

        pass
   
