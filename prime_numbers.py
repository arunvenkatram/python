#!/bin/python
import sys
def primenumber(value):
    for i in range(2,value):
        if (value % i) == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        print (value)
ran = sys.argv[1]
rang = int(ran)
for number in range(3,rang):
    primenumber(number)