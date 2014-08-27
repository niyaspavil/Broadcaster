
class OAuthHandler(object):

   def __init__(self, cs_key=None, cs_secret=None):
      self.access_token=self.Access_Token()

   def get_authorization_url(self):
      return "test_url"

   def get_access_token(self, pin):
      self.access_token.set_access("user999", "user999")

   def set_access_token(self, usr_key, usr_secret):
      self.access_token.set_access(usr_key, usr_secret)

   class Access_Token(object):
      def __init__(self):
         self.key=""
         self.secret=""

      def set_access(self, key, secret):
         self.key=key
         self.secret=secret
   
class API(object):
   
   def __init__(self, auth):
      pass

   def update_status(self, msg):
      pass
