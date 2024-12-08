#!/usr/bin/env python

import re 
from itertools import zip_longest
from functools import cmp_to_key

data = open("input/day_13.txt").read()
pairs = data.split("\n\n")

pairs = [(eval(x.splitlines()[0]), eval(x.splitlines()[1])) for x in pairs]

def compare(left, right):
	for litem, ritem in zip_longest(left, right, fillvalue=None):
		result=None
		
		if isinstance(litem, int) and isinstance(ritem, int):
			if litem < ritem: 
				return True 
			if ritem < litem:
				return False

		elif isinstance(litem, int) and isinstance(ritem, list):
			result=compare([litem], ritem)
		elif isinstance(litem, list) and isinstance(ritem, int):
			result=compare(litem, [ritem])
		elif isinstance(litem, list) and isinstance(ritem, list):
			result=compare(litem, ritem)
		elif litem==None:
			return True
		elif ritem == None:
			return False

		if not result == None:
			return result

result=0
received=[]


for index, pair in enumerate(pairs):
    
    if compare(*pair):
        result+=(index+1)

    
print("one", result)

packets = [p for pair in pairs for p in pair]
two = 1 + sum(1 for p in packets if compare(p, [[2]]))
six = 2 + sum(1 for p in packets if compare(p, [[6]]))

print("two", two * six)