#!/usr/bin/env python

data = "input/day_03.txt"

result_1=0
with open(data, "r") as f:
    lines = f.read().splitlines()
    # first
    for line in lines:
        first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
        wrong = [*first.intersection(second)][0]
        if wrong.upper() == wrong:
            result_1+=ord(wrong)-38
        else:
            result_1+=ord(wrong)-96
    # second
    i=0
    result_2=0
    while i+3 <= len(lines):
        badge = set(lines[i]).intersection(set(lines[i+1]), set(lines[i+2]))
        badge = [*badge][0]
        if badge.upper() == badge:
            result_2+=ord(badge)-38
        else:
            result_2+=ord(badge)-96
        i+=3
            
            
print("one", result_1)
print("two", result_2)
