import argparse

argument1 = 'helloo -> twitter,fb,linkdin'

argument2 = "hello -fb,-twitter,-linkdin"


parser = argparse.ArgumentParser(prefix_chars='->')
parser.add_argument("message")
parser.add_argument("->chanels")


args=parser.parse_args(.split())
print args.message
print args.chanels
