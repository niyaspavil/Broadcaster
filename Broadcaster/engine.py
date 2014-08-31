

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
        codestring = cp.get(section, 'strings')
        codelist = codestring.split(",")
        if code in codelist:
            return cp.get(section, 'channel')
            break
    return channel


# Funtion to convert list of channels given by user,
# ie userslist to a dictionary such that
# each of channel inputed by user maps to it's actual channel name.
def dict (userslist):
    d = {}
    for i in userslist:
        d [i] = decode (i)
    # d is the dictionary
    #  mentioned in the above description.
    return d



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



# Accepts the "[[facebook],[twitter],[blog],[0]]" thing from channel.py
# Accept the data in "{fb:facebook, linkedin:0, twitter:twitter}" form 
# from the dict.py
# Appents the invalid inputs to [0], inputs which means facebook to [fb] etc.
def sort (d):
    c = channel ()
    for i in range (0, len (c)):
        for j in d.keys():
            if c[i][0] == d[j]:
                c[i].append(j)
                del d[j]
    return c
    


# Main module of engine.
# Recives input from user in this form
#                 ['hai'[fb, twitter, linkedin]]
# Calls all the valid plugins.
def engine (ui):
    msg, userslist = ui
    d = dict (userslist)
    tocall = sort (d)

    reportoui = tocall [-1]
    reportoui = [reportoui]

    for i in tocall[:-1]:
        if len (i) > 1:
            x = __import__ (i[0])
            y = x.post(msg)
            j = i
            j.append (y)
            print j
            reportoui.append(j)

    return reportoui

