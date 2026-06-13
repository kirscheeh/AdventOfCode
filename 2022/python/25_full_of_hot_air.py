#!/usr/bin/env python

numbers = open("input/day_25.txt").read().splitlines()

digits= {"2":2, "1":1, "0":0, "-":-1, "=":-2}

total=0
for num in numbers:
    num = num[::-1]
    for i, c in enumerate(num):
        h = digits[c]*(5**i)
        total+=h
        
res=""
encode="012=-"

while total: # why tho
    res+=encode[total%5]
    total=(total+2)//5
print(res[::-1])
    

