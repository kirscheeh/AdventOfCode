#!/usr/bin/env python

data = "input/day_02.txt"

# A, X Rock 1
# B, Y Paper 2
# C, Z Scissors 3

dic_shapes = {"X":"A", "Y":"B", "Z":"C"}
dic_scores= {"A":1, "B":2, "C":3}

dic_win =  {"A":"C", "B":"A", "C":"B"}
dic_lose = {"A":"B", "B":"C", "C":"A"}

with open(data) as f:
    lines = f.read().splitlines()
    output=[]
    for line in lines:
        a, b = line.split(" ")
        output.append((a, dic_shapes[b]))

result_1=0
result_2=0
for op, me in output:
    # one
    if op == me: # draw
        tmp = 3 + dic_scores[me]
    elif (me, op) in [("A", "C"), ("C", "B"), ("B", "A")]:
        tmp = 6 + dic_scores[me]
    else:
        tmp = dic_scores[me]
    result_1+=tmp 
    
    # two
    if me == "B": # draw
        tmp = 3+ dic_scores[op]
    elif me=="A": # loose
        tmp = dic_scores[dic_win[op]]
    else:
        tmp = 6 + dic_scores[dic_lose[op]]
    result_2+=tmp
    
        
    

print("one", result_1)    
print("two", result_2)
    