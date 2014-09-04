
class Ui(object):

    def __init__(self):
    
        """
                     This is a constructor for read user input
        """
        
        raise NotImplementedError
    
    def get_mesg_and_chanl(self):
        
        """
                     This is a abstract Function for get message and channel list from user input
        """

        raise NotImplementedError
    
    def display_error(self,error):
        
        """
                     This is an abstract function for display the error.
        """
	raise NotImplementedError
    
    def prompt(self,content):

	"""

		     This abstract function will prompt some content to the user and return reply to the engine
	"""

	raise NotImplementedError
