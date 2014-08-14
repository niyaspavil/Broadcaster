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



class terminal_ui(ui):
    
    def __init__(self):
        
        "read user input from the terminal"

        parser = argparse.ArgumentParser()

        parser.add_argument( '-mesg', '--message',type=str,required=True, help='Message to be sended')
        parser.add_argument( '-chanl', '--channels',type= str, required=True, help='Channel list to send the message',)
        args= parser.parse_args()
        self.message =args.message
        self.channels = args.channels

    
        
        
        
        
    
    def get_message_and_channel(self):
        
        "separate message and channel list from user input"
        channel_list=self.channels.split()
        return (self.message,channel_list)
    
    def display_status_and_error(self):
        
        "display the status and error return from other levels"

        pass
