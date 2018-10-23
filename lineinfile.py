#!/bin/python
import argparse
parser = argparse.ArgumentParser("Read specific line in from a file")
parser.add_argument('filename', help='the file to read')
parser.add_argument('line', help='The line to read')
args=parser.parse_args()
try:
    content = open(args.filename, 'r').readlines()
    line = content[int(args.line) -1]
except IOError as err:
    print("Error: File does not exist")
except IndexError as err:
    print("Line %s not found in file %s" %(args.line, args.filename))
else:
    print(line)
