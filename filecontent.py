#!/bin/python
filename = raw_input("Enter the file name: ").strip()
content = raw_input("Enter the contents: ")
with open(filename, 'w') as file:
    file.write(content)
