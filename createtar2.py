#!/bin/python
import tarfile
import os
import subprocess
os.chdir("/vagrant/python_codes/")
t = tarfile.open("pycodes.tar", 'w')
temp = subprocess.check_output("ls")
arunlist = temp.split()
for files in arunlist:
    t.add(files)
t.close