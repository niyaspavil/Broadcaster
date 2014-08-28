# Funtion to convert list of channels given by user ie ul to a dictionary such that each of channel inputed by user maps to it's actual channel name.
def dict (ul):
    from decode import decode
    d = {}
    for i in ul:
        d [i] = decode (i)
    return d
