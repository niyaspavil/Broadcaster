class plugin_mocker(object):
    
    def __init__(self, chnl, user, msg):
        self.post_called=False
        self.chnl=chnl
        self.msg=msg
        
    def post(self):
        self.post_called=True
