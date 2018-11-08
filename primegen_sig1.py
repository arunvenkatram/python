#!/bin/python3.6
#this program will calculate prime number, but will start printing only when we supply "pkill -HUP primegen3.py in another terminal"
from time import sleep
from signal import *
def isprime(n):
    sleep(0.1)
    x=2
    while(x*x) <= n:
        if not n % x:
            return False
            break
        x += 1
    return True
number = 1
debug = False
def sighup_handler(signum, frame):
    global debug # if this line is not there, then it will  take arbitary value for debug as the variable is defined outside the function.
    debug = not debug
signal(SIGHUP, sighup_handler)
primelist=[]
signal(SIGINT, SIG_IGN)
signal(SIGTERM, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
while True:
    if isprime(number):
        if debug:
            print(number)
        primelist.append(number)
    number += 1
