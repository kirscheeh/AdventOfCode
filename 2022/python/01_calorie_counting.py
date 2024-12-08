#!/usr/bin/env python

DATA: str = "input/day_01.txt"

with open(DATA) as f:
    elves = f.read().split("\n\n")
    
calories=lambda x: [sum(map(int, sub.split("\n"))) for sub in x]

top3 = sorted(calories(elves), reverse=True)[:3]
print("one", max(top3))
print("two", sum(top3))
