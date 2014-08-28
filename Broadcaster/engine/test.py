from dict import dict
x = "===================================================================================================="
print "\n\n%s" %x
print "Testing dict: \n--------------"
d = dict (["facebook", "twitter", "mail", "vinayak", "78", "fb", "tweet", "email", "sdhf"])
print d
print "\n"

from sort import sort
print "Testing sort: \n--------------"
print sort (d)
print "\n"

from mockplugin import engine
print "Testing engine: \n----------------"
engine (['hii', ["facebook",  "mail", "vinayak", "78", "fb", "email", "sdhf"]])


print "%s\n\n" %x
