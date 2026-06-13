#!/usr/bin/env python3

import pandas as pd
import sys

tiles = open("input/day_23.txt", "r").read().splitlines()

class Elves:
    def __init__(self, pos):
        self.position = pos # curretn position on grid
        self.directions:list = ["N", "S", "W", "E"] # order of directions to check
        self.proposal:str="" # latest proposal
        self.endpoint=False # is this elve at the endpoint?
        self.allowed=False # allowed to proceed with proposal
        self.previous_proposal = self.proposal

    def propose(self, grid:list, occupied:list) -> str:
        self.previous_proposal = self.proposal
        print(self.position)
        for dirc in self.directions:
            x, y = self.position
            if dirc == "N":
                if not [x-1, y] in occupied and not [x-1,y+1] in occupied and not [x-1,y-1] in occupied:
                    self.proposal = "N"
                    self.set_allowed()
                    return "N"
            elif dirc == "S":
                if not [x+1,y] in occupied and not [x+1,y+1] in occupied and not [x+1,y-1] in occupied:
                    self.proposal = "S"
                    self.set_allowed()
                    return "S"
            elif dirc == "W":
                if not [x+1,y-1] in occupied and not [x,y-1] in occupied and not [x-1,y-1] in occupied:
                    self.proposal ="W"
                    self.set_allowed()
                    return "W"
            elif dirc == "E":
                if not [x+1,y+1] in occupied and not [x,y+1] in occupied and not [x+1,y+1] in occupied:
                    self.proposal = "E"
                    self.set_allowed()
                    return "E"

    def set_allowed(self):
        if self.previous_proposal == self.proposal:
            self.allowed = False
        else:
            self.allowed=True

    def get_position(self) -> list:
        return self.position

    def get_proposal(self) -> str:
        return self.proposal

    def move(self):
        if self.allowed:
            if self.proposal == "N":
                self.position = [self.position[0]-1, self.position[1]]
            elif self.proposal == "S":
                self.position = [self.position[0]+1, self.position[1]]
            elif self.proposal == "W":
                self.position = [self.position[0], self.position[1]-1]
            else:
                self.position = [self.position[0], self.position[1]+1]

    def check_endpoint(self, grid) -> bool:
        x, y = self.position
        to_check = [[x+1, y], [x-1,y], [x+1, y-1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x, y+1], [x,y-1]]
        for x_check, y_check in to_check:
            if grid[x_check][y_check] =="#":
                self.endpoint=True
                return True
        self.endpoint=False
        return False


elves=[]
for row in range(len(tiles)):
    for gollum in range(len(tiles[row])):
        if tiles[row][gollum] == "#":
            dobby = Elves(pos=[row, gollum])
            elves.append(dobby)

for elf in elves:
    print(elf.get_position())

while True:
    next_grid = tiles.copy()
    occupied = [elf.get_position() for elf in elves]

    for line in next_grid:
        print(line)

    for elf in elves:
        elf.propose(next_grid, occupied)
    print(occupied)
    proposals = [elf.get_proposal() for elf in elves]

    print(proposals)

    for elf in elves:
        elf.move()

    positions = [elf.get_position() for elf in elves]
    print(positions)
    for row in range(len(next_grid)):
        to_print = ""
        for gollum in range(len(next_grid[row])):
            if [row, gollum] in positions:
                to_print += "#"
            else:
                to_print+="."
        print(to_print)


    input()
    # proposal
    #for elf in elves:
    #    print(elf.propose())
