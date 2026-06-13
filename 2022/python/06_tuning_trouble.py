#!/usr/bin/env python

data = "input/day_06.txt"

with open(data) as f:
    devices = f.read().splitlines()
    windowsize = 14, # one 4
    for line in devices:
        for i in range(len(line)-windowsize):
            if len(set(line[i:i+windowsize])) == windowsize:
                print(i+windowsize)
                break
