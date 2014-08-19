
class engin(object):

    def __init__(self,tup):
                 
                 self.message = tup[0]
                 self.channel_list = tup[1]

    def get_response(self):
        
        return " i get values... message is  {} and channel_list is {}".format(self.message,self.channel_list)
