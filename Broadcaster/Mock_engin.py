
class engin(object):

    def __init__(self,tup):
                 
                 self.message = tup[0]
                 self.channel_list = tup[1]

    def get_response(self):
        
        return "\n\n\n I get values. Message is '{}' and Channel_list is '{}'\n\n\n".format(self.message,self.channel_list)
