# Main module of engine.
# Recives input from user in this form
#                 ['hai'[fb, twitter, linkedin]]
# Calls all the valid plugins.
# Returns 

def engine (ui):
    msg, userslist = ui
    from sort import sort
    from dict import dict
    d = dict (userslist)
    tocall = sort (d)

    reportoui = c[-1]
    reportoui = reportoui [-1:]
    reportoui = [reportoui]

    for i in tocall[:-1]:
        if len (i) > 1:
            x = import(i[0])
            x.post(msg)

    return reportoui
