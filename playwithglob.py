#!/bin/python
import os
import glob
import shutil
import json
try:
    os.mkdir('/vagrant/python_codes/processed')
except OSError:
    print('directory already exist')
# get list of receipts
receipts = glob.glob('/vagrant/python_codes/recepits/new/receipt-[0-9]*.json')
subtotal = 0.0
#iterate over the receipts
for path in receipts:
    with open(path) as file:
        content=json.load(file)
        #read the content and tally a subtotal
        subtotal = subtotal + float(content['value'])
    name=path.split('/')[-1]
    destination="/vagrant/python_codes/processed/%s" % name
    #move those file to the processed directory
    shutil.move(path , destination)
    #print the processed file
    print("Moved %s to %s" % (path, destination))
    #print the subtotal of all the processed receipts
print("Subtotal is %.2f" %subtotal)
