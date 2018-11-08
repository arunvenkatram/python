#!/bin/python
from time import sleep
from signal import *
def isprime(n):
    sleep(0.1)
    x=2
    while (x*x) <= n:
        if not n % x:
            return True
            break
        x += 1
    return False
def totalprime(signal, frame):
    print("Total number of prime numbers counted is %d" %len(prime_list))
def displayprime(signal, frame):
    global debug
    print("toggling prime number display")
    debug = not debug
signal(SIGUSR1, totalprime)
signal(SIGUSR2, displayprime)
debug=True
number = 1
prime_list = []
while True:
    if isprime(number):
        if debug:
            print number
        prime_list.append(number)
    number += 1