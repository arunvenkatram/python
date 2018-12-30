#!/bin/python
from sys import argv
script, user = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user, script)
print "What is your age?"
age = raw_input(prompt).strip()
age = int(age)
print "Where do you live?"
place = raw_input(prompt)
print("Alright, I know your age is %d and you live in %s" %(age, place))
