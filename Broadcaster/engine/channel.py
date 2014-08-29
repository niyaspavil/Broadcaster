# This is the module to read data stored in channel.ini file.
# The object returned by the list is something similar to:
# [[facebook],[twitter],[blog],[0]]
# The [0] in the end is useful for implementation of the module named sort.

def channel ():
    import ConfigParser
    cp =  ConfigParser.ConfigParser()
    cp.read("channel.ini")
    channels = []

    for section in cp.sections():
        channels.append(cp.get(section, 'channel'))

    for i in range (0, len(channels)):
        channels [i] = [channels [i]]
    channels.append([0])
    return channels
