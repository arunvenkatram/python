#!/bin/python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-a", "--age", dest="age", type="int", default=20, help="Enter your age")
parser.add_option("-n", "--name", dest="name", help="enter your name")
(options, args) = parser.parse_args()
print("Name is %s" %options.name)
print("Age is %d" %options.age)
print("Entra arguments passed without any options are %s" %str(args))