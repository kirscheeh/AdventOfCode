#!/usr/bin/env python3

import sys
import pandas as pd

valley = open("input/day_24.txt", "r").read().splitlines()

width = len(valley[0])
length = len(valley)

borders = [[0,i] for i in range(width)] + [[length-1, i] for i in range(width)]+[[i, 0] for i in range(length)] + [[i, width-1] for i in range(length)]
borders.remove([length-1, width-2])

FINISH=[length-1, width-2]
expedition=[0, 1]

# get initial position of blizzar
up:list = []
down:list = []
left:list = []
right:list = []
board:list = []
for row in range(1, len(valley)):
    for gollum in range(len(valley[row])):
        board.append([row, gollum])
        if valley[row][gollum] == "^":
            up.append([row, gollum])
        elif valley[row][gollum] == ">":
            right.append([row, gollum])
        elif valley[row][gollum] == "<":
            left.append([row, gollum])
        elif valley[row][gollum] == "v":
            down.append([row, gollum])
        else:
            pass

# move blizzards one iteration
def one_minute():
    for blizz in down:
        blizz[0] +=1
        if blizz in borders:
            blizz[0] = 1

    for blizz in up:
        blizz[0] -=1
        if blizz in borders:
            blizz[0] = length-2

    for blizz in right:
        blizz[1] +=1
        if blizz in borders:
            blizz[1] = 1

    for blizz in left:
        blizz[1] -= 1
        if blizz in borders:
            blizz[1] = width-2

# print current valley
def print_valley():
    for row in range(length):
        to_print=""
        for gollum in range(width):
            if [row, gollum] in borders and not [row, gollum] == expedition:
                to_print += "#"
            elif [row, gollum] in up:
                to_print+="^"
            elif [row, gollum] in down:
                to_print += "v"
            elif [row, gollum] in left:
                to_print+="<"
            elif [row, gollum] in right:
                to_print+=">"
            elif [row, gollum] == expedition:
                to_print+="E"
            else:
                to_print+="."
        print(to_print)


# check what expedition should do
def check_paths():
    global expedition
    occ = borders+up+down+left+right

    options=[]
    # check down
    # check right
    if [expedition[0], expedition[1]+1] not in occ and [expedition[0], expedition[1]+1] in board:
        options.append([expedition[0], expedition[1]+1])
        print("right")

    if [expedition[0]+1, expedition[1]] not in occ and [expedition[0]+1, expedition[1]] in board:
        options.append([expedition[0]+1, expedition[1]])
        print("down")


    # check left
    if [expedition[0], expedition[1]-1] not in occ and [expedition[0], expedition[1]-1] in board:
        options.append([expedition[0], expedition[1]-1])
        print("left")
# check up
    if [expedition[0]-1, expedition[1]] not in occ and [expedition[0]-1, expedition[1]] in board:
        options.append([expedition[0]-1, expedition[1]])
        print("up")

    print()
    try:
        expedition = options[0]
    except Exception:
        expedition=expedition

iteration=0
while True:

    check_paths()
    #print_valley()
    one_minute()

    if expedition == FINISH:
        print(iteration)
        break

    iteration+=1
