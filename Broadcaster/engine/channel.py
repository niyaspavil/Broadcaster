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
