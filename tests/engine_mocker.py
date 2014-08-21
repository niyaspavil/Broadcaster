
conf = {'consumer_key':'BCxhHxyTR4vHtKXqa7jSTicv4', 'cosumer_secret':'sCpiNzjR9MTcFHbVWkuukm0ucKbYXnyv1ZdZQpDlRXAyzSMfpy', 'user_token':'2736495205-8f8yRTQeQ7JFhQHsqfSPWtl2iDafsJiiPsymOW1', 'user_token_secret':'vbzYBj1AbX4FZrrDtT2caQCVPt16Di0LTvsVArXTjQ3Ht'}

class Engine(object):
    """Mocker class for engine"""
    
    def __init__(self):
        """nothing special... :P"""
        self.plugin="twitter"

    def get_attrib(self, option):
        """return attribute from conf"""
        return conf.get(option)

    def set_attrib(self, option, value):
        """stores option-value pair to the conf"""
        conf[option]=value

    def prompt_user(self, msg, type):
        """prompts user with msg and return the input from user"""
        return 999
