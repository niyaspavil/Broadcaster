def post(msg):
    print "\n~~~~~~Entered Mail mock plugin~~~~~~"    
    print "The mock twitter plugin have been called and \" %s \" is given as an input to it." %msg

    if len(msg) >= 10:
        return "Mail is happy"
    else:
        return "Mail is sad"
        
    print "~~~~~~Exiting Mail mock plugin~~~~~~"
