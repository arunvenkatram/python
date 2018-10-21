#!/bin/python
import subprocess
code = subprocess.call(['ls', '-l'])
if code == 0:
    print("command completed successfully")
else:
    print("command failed")
output = subprocess.check_output(['pwd'])
print output
