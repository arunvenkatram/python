#!/bin/python
from sys import argv
from os.path import exists
script, source, dest = argv
print("Going to copy contents from %s to %s file" %(source, dest))
sfile = open(source)
sdata = sfile.read()
print("input file is %d bytes long" % len(sdata))
print("checking if the output file exists: %r" % exists(dest))
print("Ready, hit ENTER to continue, CTRL+C to cancel")
raw_input()
print("Opening %s file for writing" %dest)
dfile = open(dest, "a+")
print "Writing data"
dfile.write(sdata)
print("Completed writing")
sfile.close()
dfile.close()
