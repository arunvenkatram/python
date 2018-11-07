#!/bin/python
import sys
import tarfile
if len(sys.argv) < 2:
    list = ["."]
else:
    list = sys.argv[1:]
with tarfile.open("/tmp/test.tar", 'w') as t:
    for file in list:
        t.add(file)
