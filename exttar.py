#!/bin/python
import tarfile
import os
import subprocess
t = tarfile.open("/tmp/arun/pycodes.tar")
os.chdir("/tmp/arun/")
t.extractall()
subprocess.Popen(['ls', '/tmp/arun'])