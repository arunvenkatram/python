#!/bin/python
import os
pi = 22.0/7.0
digits = os.getenv("DIGITS") or 2
print('%.*f' %(int(digits), pi))