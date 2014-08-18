from Broadcaster import twitter

def test_twitter_plugin(msg="The funny dummy tweet~!!.."):
    """test for twitter plugin"""
    tmp_plug=twitter.Tweet(msg)
    assert tmp_plug.post()==True

test_twitter_plugin()
test_twitter_plugin("The real tweet!!!")
