#!/usr/bin/env python

movements = open("input/day_09.txt").read().splitlines()
movements = [x.split() for x in movements]

def check_touchy(head, tail):
    if head == tail:
        return True
    
    if head[1] == tail[1]:
        if head[0]-1 == tail[0]:
            return True 
        if head[0]+1 == tail[0]:
            return True
    
    if head[0] == tail[0]:
        if head[1]-1==tail[1]:
            return True
        if head[1]+1 == tail[1]:
            return True
    
    # diagonal
    if (head[0]-1 == tail[0] and head[1]-1==tail[1]) or (head[0]+1 == tail[0] and head[1]+1==tail[1]) or (head[0]-1 == tail[0] and head[1]+1==tail[1]) or (head[0]+1 == tail[0] and head[1]-1==tail[1]): 
        return True
    
    return False

def update_tail(head, tail):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1]+=1
        else:
            tail[1]-=1
    
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0]+=1
        else:
            tail[0]-=1
    else:
        if head[0] > tail[0] and head[1] < tail[1]:
            tail[0] +=1
            tail[1] -=1
        elif head[0] > tail[0] and head[1] > tail[1]:
            tail[0] +=1
            tail[1] +=1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -=1
            tail[1] -=1
        else:
            tail[0] -=1
            tail[1] +=1
    return tail

# x, y
curr_head=[0,0]
curr_tail=[0,0]

tails=[[0,0] for i in range(9)]

tail_visits_1=set()
tail_visits_9=set()

for direction, stepsize in movements:
    for step in range(int(stepsize)):
        if direction == "R":
            curr_head[0]+=1
        elif direction=="L":
            curr_head[0]-=1
        elif direction=="U":
            curr_head[1]-=1
        else:
            curr_head[1]+=1
        
        if not check_touchy(curr_head, curr_tail):
            curr_tail = update_tail(curr_head, curr_tail)
            
        tail_visits_1.add(tuple(curr_tail))
        
        if not check_touchy(curr_head, tails[0]):
            tails[0] = update_tail(curr_head, tails[0])
        for i in range(len(tails)-1):
            if not check_touchy(tails[i], tails[i+1]):
                tails[i+1] = update_tail(tails[i], tails[i+1])

        tail_visits_9.add(tuple(tails[-1]))
        
print("one", len(tail_visits_1))
print("two", len(tail_visits_9))
            