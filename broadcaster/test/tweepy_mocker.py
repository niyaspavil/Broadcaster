class OAuthHandler(object):

   def __init__(self, cs_key=None, cs_secret=None):
      self.cs_key=cs_key
      self.cs_secret=cs_secret
      self.access_token=self.Access_Token()

   def get_authorization_url(self):
      if self.cs_key=="consumer999" and self.cs_secret=="consumer999":
         return ""
      else:
         raise TweepError(HttpError())
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
      self.auth=auth

   def update_status(self, msg):
      ck=self.auth.cs_key
      cs=self.auth.cs_secret
      uk=self.auth.access_token.key
      us=self.auth.access_token.secret
      if ck=="consumer999" and cs=="consumer999" and uk=="user999" and us=="user999":
         return True
      else:
         raise TweepError([{"message":"failed","code":32}])

class TweepError(Exception):
   def __init__(self, error):
      self.message=error
   def __str__(self):
      return ""

class HttpError(Exception):
   def __init__(self):
      pass
