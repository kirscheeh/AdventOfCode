<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3

import re

data = open("input/day_14.txt").read().splitlines()


rocks = []
for rock in data:
    pos = re.findall("([0-9]{1,}),([0-9]{1,})", rock)
    rocks.append(pos)
print(rocks)
walls = []

deepest=0
widest=0
for rock in rocks:
    for index in range(len(rock)-1):
        curr, nex = rock[index], rock[index+1]
        if int(curr[0]) > widest:
            widest=int(curr[0])
        if int(curr[1]) > deepest:
            deepest=int(curr[1])
        if curr[0] == nex[0]:
            for length in range(min(int(curr[1]), int(nex[1])), max(int(curr[1]), int(nex[1]))+1):
                walls.append([int(curr[0]), length])
        elif curr[1] == nex[1]:
            for length in range(min(int(curr[0]), int(nex[0])), max(int(curr[0]), int(nex[0]))+1):
                walls.append([length, int(curr[1])])

#walls.extend
occupied = walls.copy()
steps=0
print(occupied)
snow = []
while True:

    new_snow = [500,0]
    while not new_snow in occupied:
        new_snow[1]+=1


    new_snow = [new_snow[0], new_snow[1]-1]

    if new_snow not in occupied:
        occupied.append(new_snow)
        snow.append(new_snow)
    else:
        while True:
            left =  [new_snow[0]-1, new_snow[1]]
            right =  [new_snow[0]+1, new_snow[1]]
            print(left, right)
            if left not in occupied:
                new_snow = left
            elif right not in occupied:
                new_snow = right
            else:
                break

            if new_snow[0] >= widest:
                break

            if new_snow[1] >= deepest or new_snow[1] < 0:
                break

            if not [left[0]+1, left[1]] in occupied:
                occupied.append([left[0]+1, left[1]])
                break

            elif not [right[0]-1, right[1]] in occupied:
                occupied.append([right[0]-1, right[1]])
                break


    print(new_snow)
    if new_snow[0] >= widest:
        print(steps)
        break

    if new_snow[1] >= deepest or new_snow[1]<0:
        print(steps)
        break
    input()
>>>>>>> eddcac0 (remaining days)
