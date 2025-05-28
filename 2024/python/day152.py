#!/usr/bin/env python3
import time
grid, move_order = open("/home/kirscheeh/repositories/AdventOfCode/inputs/2024/day15.txt").read().split("\n\n")

GRID_LENGTH=0
GRID_WIDTH=0
WALLS=set()

def read_grid(grid:str, part2:bool = False) -> tuple[set, set, ()]:
    boxes: set = set()
    global GRID_LENGTH, GRID_WIDTH
    for row, content in enumerate(grid.split()):
        gollum=0
        for _, cell in enumerate(content):
            match cell:
                case "#":
                    WALLS.add(gollum+1j*row)
                    if part2:
                        WALLS.add((gollum+1)+1j*row)
                        gollum+=1
                case "O":
                    boxes.add(gollum+1j*row)
                    if part2:
                        gollum+=1
                case "@":
                    robot = gollum+1j*row
                    if part2:
                        gollum+=1
                case ".":
                    if part2:
                        gollum+=1

            gollum+=1

    GRID_WIDTH=gollum
    GRID_LENGTH=row+1
    return boxes, robot

def move_box(position, boxes, direction, already_moved) -> tuple[set, bool]:
    if position+direction in boxes:
        movable, boxes = move_box(position+direction, boxes, direction, True)
        if movable and not already_moved:
            boxes.remove(position)
        if not movable:
            return False, boxes
    elif position+direction in WALLS:
        return False, boxes
    else:
        boxes.add(position+direction)
        if not already_moved:
            boxes.remove(position)
    return True, boxes

def print_warehouse(boxes, robot, part2:bool=False) -> None:
    tmp = ""
    for row in range(GRID_LENGTH):
        open_bracket=False
        gollum=0
        #for _ in range(GRID_WIDTH):
        while gollum <= GRID_WIDTH:
            if gollum+1j*row in WALLS:
               tmp += "#"
            elif (gollum+1j*row) in boxes:
                if part2:
                    tmp+="[]"
                    gollum+=1
                else:
                    tmp += "O"
            elif gollum+1j*row == robot:
                tmp += "\033[38;2;0;255;255m@\033[38;2;255;0;0m"
                if part2:
                    pass #tmp+="."
                #tmp += u"\U0001F923"
            else:
                tmp += "."
            gollum+=1
        tmp += "\n"
    print(tmp)#, end="\r")
    #time.sleep(0.02)

def follow_move_order(move_order, boxes, robot, part2):
    for move in move_order.strip():
        print(move, boxes)
        if move == "\n":
            continue
        direction = {">": 1+0j, "<":-1+0j, "^": -1j, "v": 1j}[move]

        print(robot)
        if robot+direction in WALLS:
            continue
        elif (robot+direction) in boxes:
            movable, boxes = move_box(robot+direction, boxes, direction, False)
            if movable:
                robot += direction
        else:
            robot += direction
        print_warehouse(boxes, robot, part2)
        input()
    return boxes, robot

def calculate_sum(boxes:set) -> int:
    result = 0
    for box, typ  in boxes:
        if typ in ["O", "["]:
            gollum, row = box.real, box.imag
            result += row*100+gollum
    return int(result)


        
part2=False
boxes, robot = read_grid(grid, part2)
print_warehouse(boxes, robot, part2)
boxes_after_move, robot = follow_move_order(move_order, boxes, robot, part2)
#print_warehouse(boxes_after_move, robot)
#print("Part 1", calculate_sum(boxes_after_move))
