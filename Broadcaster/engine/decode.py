# A function to return 'facebook' if given fb etc
# Returns 0 if given an invalid code.

def decode (code):
    import ConfigParser
    cp =  ConfigParser.ConfigParser()
    cp.read("channel.ini")
    channel = 0

# Channel.ini file is read by the variable cp.
# value of channel is set to be 0. 
# It would be changed after the loop below if the input is valid.

    for section in cp.sections():
        if code in cp.get(section, 'strings'):
            channel = cp.get (section, 'channel')
            break
            
    return channel
