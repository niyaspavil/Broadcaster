def engine (ui):
    msg, ul = ui
    from sort import sort
    from dict import dict
    d = dict (ul)
    c = sort (d)

    for i in c[:-1]:
        if len i > 1:
            x = import(i[0])
            x.post(msg)
    return c
