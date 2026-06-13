#!/usr/bin/env python

data = "input/day_04.txt"

counter_0=0
counter_1=0
with open(data) as f:
    lines = f.read().splitlines()
    
    for line in lines:
        first, second = line.split(",")
        first = first.split("-")
        second=second.split("-")
        list_first = [i for i in range(int(first[0]), int(first[1])+1)]
        list_second = [i for i in range(int(second[0]), int(second[1])+1)]
        if all(item in list_first for item in list_second) or all(item in list_second for item in list_first):
            counter_0+=1
            
        if len(set(list_first).intersection(list_second)) >0:
            counter_1+=1
print(counter_0)
print(counter_1)