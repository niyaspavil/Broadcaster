
class OAuthHandler(object):

   def __init__(self, cs_key=None, cs_secret=None):
      pass

   def get_authorization_url(self):
      return "test_url"

   def get_access_token(self, pin):
      self.access_token=self.Access_Token()

   class Access_Token(object):
      def __init__(self):
         self.key="user999"
         self.secret="user999"
