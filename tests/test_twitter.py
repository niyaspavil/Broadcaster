import random
import string
from Broadcaster import twitter

def test_twitter_plugin(msg=''.join(random.choice(string.lowercase) for x in range(10))):
    """test for twitter plugin"""
    tmp_plug=twitter.twitter (msg)
    assert tmp_plug.post()==True

