#!/usr/bin/env python3

import sys
import re

possibilities={}
valves = open("input/day_16.txt", "r").read().splitlines()

for valve in valves:
    origin = re.findall("Valve ([A-Z]{2}) has", valve)
    rate = re.findall("rate=([0-9]{,5})", valve)
    dest = re.findall("to valves? (.*)", valve)


    print(type(origin[0]), int(rate[0]))
    possibilities[origin[0]] = {"rate":int(rate[0]), "dest":dest[0].split(","), "status":False}

print(possibilities)
