#!/bin/python3.6
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
#the below code is responsible for pkill -HUP signal
debug = True
def sighup_handler(signum, frame):
    global debug # if this line is not there, then it will  take arbitary value for debug as the variable is defined outside the function.
    debug = not debug
signal(SIGHUP, sighup_handler)
#SIGUSER1 reports current status
def report_status(signum, frame):
    global primelist
    print("Number of prime numbers found as of now is" %len(primelist))
signal(SIGUSR1, report_status)
################ pkill -USR1 primegen_sig2.py
primelist=[]
while True:
    if isprime(number):
        if debug:
            print(number)
        primelist.append(number)
    number += 1
