import re 
import numpy as np
import utils
puzzle = open("inputs/2024/day04.txt").read().splitlines()

positions = {"X":[], "M":[], "A":[], "S":[]}

for row, content in enumerate(puzzle):
    for gollum, letter in enumerate(content):
        if letter in positions.keys():
            positions[letter].append((row, gollum))

part1 =0
part2 = 0
for row, gollum in positions["A"]:
    #part 1
    # horizontal
    ## forward
    if (row, gollum+1) in positions['S'] and (row, gollum-1) in positions["M"] and (row, gollum-2) in positions["X"]:
        part1+=1
    ## reverse
    if (row, gollum-1) in positions['S'] and (row, gollum+1) in positions["M"] and (row, gollum+2) in positions["X"]:
        part1+=1
    # vertical
    ## forward
    if (row-2, gollum) in positions['X'] and (row-1, gollum) in positions["M"] and (row+1, gollum) in positions["S"]:
        part1+=1
    ## reverse
    if (row-1, gollum) in positions['S'] and (row+1, gollum) in positions["M"] and (row+2, gollum) in positions["X"]:
        part1+=1
    # diagonal
    ## forward down right
    if (row-2, gollum-2) in positions['X'] and (row-1, gollum-1) in positions["M"] and (row+1, gollum+1) in positions["S"]:
        part1+=1
    ## reverse up left 
    if (row-1, gollum-1) in positions['S'] and (row+1, gollum+1) in positions["M"] and (row+2, gollum+2) in positions["X"]:
        part1+=1
    ## forward up right
    if (row+2, gollum-2) in positions['X'] and (row+1, gollum-1) in positions["M"] and (row-1, gollum+1) in positions["S"]:
        part1+=1
    ## reverse down left 
    if (row+1, gollum-1) in positions['S'] and (row-1, gollum+1) in positions["M"] and (row-2, gollum+2) in positions["X"]:
        part1+=1

    # part 2
    ## forward forward, diagonal
    if (row-1, gollum-1) in positions['M'] and (row-1, gollum+1) in positions['M'] and (row+1, gollum+1) in positions['S'] and (row+1, gollum-1) in positions['S']:
        part2+=1
    ## forward reverse
    elif (row-1, gollum-1) in positions['M'] and (row+1, gollum-1) in positions['M'] and (row+1, gollum+1) in positions['S'] and (row-1, gollum+1) in positions['S']:
        part2+=1

     ## reverse forward
    elif (row+1, gollum-1) in positions['M'] and (row+1, gollum+1) in positions['M'] and (row-1, gollum-1) in positions['S'] and (row-1, gollum+1) in positions['S']:
        part2+=1

    # reverse reverse
    elif (row-1, gollum+1) in positions['M'] and (row+1, gollum+1) in positions['M'] and (row+1, gollum-1) in positions['S'] and (row-1, gollum-1) in positions['S']:
        part2+=1

print("Part 1", part1)
print("Part 2", part2)
