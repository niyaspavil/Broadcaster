# A function to return 'facebook' if given fb etc
# Returns 0 if given an invalid code.
def decode (code):
    import ConfigParser
    cp =  ConfigParser.ConfigParser()
    cp.read("channel.ini")
    channel = 0
    for section in cp.sections():
        if code in cp.get(section, 'strings'):
            channel = cp.get (section, 'channel')
    return channel
