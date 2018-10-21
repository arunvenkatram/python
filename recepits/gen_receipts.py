#!/bin/python
import random
import json
import os
count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open("/usr/share/dict/linux.words").readlines()]
arun=type(words)
arun
for identifier in range(count):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic': random.choice(words), 'value': "%.2f" %amount }
    with open('/vagrant/python_codes/recepits/new/receipt-%s.json' % identifier, 'w') as file:
         json.dump(content, file)
