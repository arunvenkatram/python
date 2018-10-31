#!/bin/python
import tarfile
import os
os.chdir("/etc")
t=tarfile.open("/tmp/arun.tar", 'w')
for file in ['hosts', 'passwd', 'fstab']:
    t.add(file)
t.close()