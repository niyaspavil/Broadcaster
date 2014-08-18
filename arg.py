import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--facebook", action="store_true")
parser.add_argument("-t", "--twitter", action="store_true")


args = parser.parse_args()
lis=[]
if args.facebook:
    lis.append("facebook")
if args.twitter:
    lis.append("twitter")
else:
    print "pls give any option"

print lis
