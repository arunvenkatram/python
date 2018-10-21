#!/bin/python
import argparse
parser = argparse.ArgumentParser(description="Read the filename in reverse")
parser.add_argument("filename" , help='enter the filename to be read')
parser.add_argument('--limit', '-l', type=int, help="number of files to read")
parser.add_argument('--version', '-v', action='version', version='1.0')
args = parser.parse_args()
#print(args)
with open(args.filename) as file:
    lines = file.readlines()
    lines.reverse()
    if args.limit:
        lines = lines[:args.limit]
    for line in lines:
        print(line.strip()[::-1])