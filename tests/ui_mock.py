msg = raw_input("Type the message: ")
channels = []
prompt = ">~"
print "Type names of channels one by one and press enter."
print "Once you finished, type stop and press enter.\n"

while True:
    a = raw_input(prompt)
    if a == "stop" or a == "n":
        break
    channels.append(a)

ui = [msg, channels]

from engine import engine
report = engine(ui)
print "\nReport from engine:"
print report
