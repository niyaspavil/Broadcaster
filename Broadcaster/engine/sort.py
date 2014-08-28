def sort (d):
    from channel import channel
    c = channel ()
    for i in range (0, len (c)):
        for j in d.keys():
            if c[i][0] == d[j]:
                c[i].append(j)
                del d[j]
    return c
    
