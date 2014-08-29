# Accepts the "[[facebook],[twitter],[blog],[0]]" thing from channel.py
# Accept the data in "{fb:facebook, linkedin:0, twitter:twitter}" form 
# from the dict.py
# Appents the invalid inputs to [0], inputs which means facebook to [fb] etc.

def sort (d):
    from channel import channel
    c = channel ()
    for i in range (0, len (c)):
        for j in d.keys():
            if c[i][0] == d[j]:
                c[i].append(j)
                del d[j]
    return c
    
