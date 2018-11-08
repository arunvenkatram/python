#!/bin/python
import sys
from signal import *
def timeout_handler(signal, frame):
    raise IOError("Did not receive response in 5 seconds")
def get_name():
    signal(SIGALRM, timeout_handler)
    alarm(5)
    n = sys.stdin.readline()
    alarm(0) # 0 means, it will not raise SIGALRM signal
    return n
print("Enter your name")
sys.stdout.flush()
try:
    name=get_name()
except IOError as err:
    print("No inputs received")
    name = "default"
print("Name received is %s" %name)