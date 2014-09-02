def post(msg):
    print "\n~~~~~~Entered Twitter mock plugin~~~~~~"    
    print "The mock twitter plugin have been called and \" %s \" is given as an input to it." %msg

    if len(msg) <= 10:
        return "Twitter is happy"
    else:
        return "Twitter is sad"
        
    print "~~~~~~Exiting twitter mock plugin~~~~~~"
