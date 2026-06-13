#!/usr/bin/env python

data = "input/day_08.txt"

with open(data) as f:
    columns = [list(map(int, list(x))) for x in f.read().splitlines()]

# make a list of lists but vertical not horizontal
rows = [[] for x in range(len(columns[0]))]
for row in columns:
    for i in range(len(row)):
        rows[i].append(row[i])
  
max_scenic=0
visible=[[True for x in columns] for row in columns[0]]

for x in range(1, len(columns[0])-1):
    for y in range(1, len(columns)-1):
        vis=False
        # part one
        # left
        if not [*filter(lambda a: a >= columns[x][y], columns[x][:y])]:
            vis=True
        # right
        if not [*filter(lambda a: a >= columns[x][y], columns[x][y+1:])]:
            vis=True
        # up
        if not [*filter(lambda a: a >= rows[y][x], rows[y][:x])]:
            vis=True
        # down
        if not [*filter(lambda a: a >= rows[y][x], rows[y][x+1:])]:
            vis=True
        visible[x][y]=vis
         
        # part two
        # left
        if y==1:
            counter_left=1
        else:
            col = columns[x][:y][::-1]
            counter_left=0
            for elem in col:
                counter_left+=1
                if elem>=columns[x][y]:
                    break
                

        # right
        if y == len(columns[0])-1:
            counter_right=1
        else:
            counter_right=0
            for elem in columns[x][y+1:]:
                counter_right+=1
                if elem>=columns[x][y]:
                    break
            
        # up
        if x==1:
            counter_up=1
        else:
            col=rows[y][:x][::-1]
            counter_up=0
            for elem in col:
                counter_up+=1
                if elem >= columns[x][y]:
                    break
          
        # down      
        if x == len(columns)-1:
            counter_down=1
        else:
            counter_down=0
            for elem in rows[y][x+1:]:
                counter_down+=1
                if elem >= columns[x][y]:
                    break
            
        
        curr_scenic = counter_down*counter_left*counter_right*counter_up
        if curr_scenic > max_scenic:
            max_scenic=curr_scenic
            
flat_list = [item for sublist in visible for item in sublist]

print(sum(flat_list))
print(max_scenic)

        
    