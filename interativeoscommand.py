#!/bin/python
import subprocess
command = raw_input("Enter the command to run: ")
command = str(command)
try:
    output = subprocess.check_output([command])
except OSError as err:
    print("error has occurred, no such file or directory.")
except subprocess.CalledProcessError as err:
    print("Error has occurred, command does not exist")
else:
    print(output)

