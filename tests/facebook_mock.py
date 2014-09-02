def post(msg):
    print "\n~~~~~~Entered Facebook mock plugin~~~~~~"    
    print "The mock facebook plugin have been called and \" %s \" is given as an input to it." %msg

    if msg [1] == "F":
        return "Facebook is sad"
    else:
        return " Facebook is happy"
        
    print "~~~~~~Exiting facebook mock plugin~~~~~~"
