
class SMTP(object):
	
    def __init__(self,server=None,port=None):
        pass
    def ehlo(self):
	pass
    def starttls(self):
	pass
    def login(self,user,pswd):
        if user == "consumer999" and pswd == "consumer999" :
           return ''
        else:
           raise SMTPAuthenticationError()
    def sendmail(self,frm,to,mail):
	if to =='consumer999':
            return ''
        elif to == 'consumer99':
            raise SMTPRecipientsRefused()
        elif to == 'consumer9':
            raise SMTPDataError()
        else:
            raise SMTPConnectError()

class SMTPAuthenticationError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return ""

class SMTPRecipientsRefused(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return ""
class SMTPDataError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return ""

class SMTPConnectError(Exception):
    def __init__(self):
        pass
