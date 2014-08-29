# Funtion to convert list of channels given by user,
# ie userslist to a dictionary such that
# each of channel inputed by user maps to it's actual channel name.

def dict (userslist):
    from decode import decode
    d = {}
    for i in userslist:
        d [i] = decode (i)

# d is the dictionary
#  mentioned in the above description.

    return d
