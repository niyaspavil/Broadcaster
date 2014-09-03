
class SMTP(object):
	
    def __init__(self,server=None,port=None):
        self.server=self.Server()

    class Server(object):
	def __init__(self):
	    pass	
	def ehlo(self):
	    pass
	def starttls(self):
	    pass
