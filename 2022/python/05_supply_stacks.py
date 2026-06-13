#!/usr/bin/env python

data = "input/day_05.txt"

import re
import pandas as pd 
import numpy as np

with open(data) as f:
    lines = f.read()
    stacks, moves = lines.split("\n\n")
    
# transform stacks in useful format: dic of queues
stacks = stacks.replace("    ", "[]")

list_of_heights=[]
for line in stacks.splitlines()[:-1]:
    height = re.findall(r"\[.*?\]", line)
    list_of_heights.append(height)

list_of_heights.reverse()
dic = {x:[] for x in range(1, 10)}
dic_2={x:[] for x in range(1, 10)}
for key, _ in dic.items():
    for l in list_of_heights:
        if l[key-1] == "[]":
            continue
        elem = l[key-1].replace("[", "").replace("]", "")
        dic[key].append(elem)
        dic_2[key].append(elem)

# transform commands in useful structure: list of tuples
commands = []
for line in moves.splitlines():
    amount, source, destination = re.findall("[0-9]{1,3}", line)
    commands.append((int(amount), int(source), int(destination)))

for amount, source, destination in commands:
    print(amount, source, destination)
    for i in range(amount):
        dic[destination].append(dic[source].pop())
    dic_2[destination].extend(dic_2[source][-amount:])
    dic_2[source] = dic_2[source][:-amount]
        
result_string = ""
for _, val in dic.items():
    result_string+=val[-1]
print("one", result_string)

result_string = ""
for _, val in dic_2.items():
    result_string+=val[-1]
print("two", result_string)
