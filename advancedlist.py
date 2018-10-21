#!/bin/python
import argparse
parser=argparse.ArgumentParser(description='search for words inluding partial words')
parser.add_argument('snippet', help='enter the partial work here')
args = parser.parse_args()
snippet=args.snippet.lower()
dict = open('/usr/share/dict/linux.words', 'r')
words=dict.readlines()
matches=[]
for word in words:
    if snippet in word.lower():
        matches.append(word)
print(matches)