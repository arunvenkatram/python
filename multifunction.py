#!/bin/python
message = raw_input("Enter the message to be echoed: ")
count = raw_input("enter the number if times to echo the message: ").strip()
if count:
    count = int(count)
def echo_func(message, count):
    while count > 0:
        print(message)
        count -=1
echo_func(message, count)