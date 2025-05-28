
#!/usr/bin/env python3
import time
grid, move_order = open("/home/kirscheeh/repositories/AdventOfCode/inputs/2024/day15.txt").read().split("\n\n")

GRID_LENGTH=0
GRID_WIDTH=0

def read_grid(grid:str, part2:bool = False) -> tuple[set, set, ()]:
    walls: set = set()
    boxes: set = set()

    global GRID_LENGTH, GRID_WIDTH

    for row, content in enumerate(grid.split()):
        for gollum, cell in enumerate(content):
            match cell:
                case "#":
                    walls.add(gollum+1j*row)
                    if part2:
                        walls.add(gollum+1+1j*row)
                case "O":
                    if part2:
                        boxes.add((gollum+1j*row, "["))
                        boxes.add((gollum+1+1j*row, "]"))
                    else:
                        boxes.add((gollum+1j*row, "O"))
                case "@":
                    robot = gollum+1j*row
    GRID_WIDTH=gollum+1
    GRID_LENGTH=row+1
    return walls, boxes, robot

def move_box(position, boxes, direction, already_moved) -> tuple[set, bool]:
    if (position+direction, "O") in boxes:
        movable, boxes = move_box(position+direction, boxes, direction, True)
        if movable and not already_moved:
            boxes.remove((position, "O"))
        if not movable:
            return False, boxes
    elif position+direction in walls:
        return False, boxes
    else:
        boxes.add((position+direction, "O"))
        if not already_moved:
            boxes.remove((position, "O"))
    return True, boxes

def print_warehouse(boxes, walls, robot) -> None:
    tmp = ""
    for row in range(GRID_LENGTH):
        for gollum in range(GRID_WIDTH):
            if gollum+1j*row in walls:
               tmp += "#"
            elif (gollum+1j*row, "O") in boxes:
                tmp += "O"
            elif gollum+1j*row == robot:
                tmp += "\033[38;2;0;255;255m@\033[38;2;255;0;0m"
                #tmp += u"\U0001F923"
            else: tmp += "."
        tmp += "\n"
    print(tmp, end="\r")
    time.sleep(0.02)

def follow_move_order(move_order, walls, boxes, robot):
    for move in move_order.strip():
        if move == "\n":
            continue
        direction = {">": 1+0j, "<":-1+0j, "^": -1j, "v": 1j}[move]
        if robot+direction in walls:
            continue
        elif (robot+direction, "O") in boxes:
            movable, boxes = move_box(robot+direction, boxes, direction, False)
            if movable:
                robot += direction
        else:
            robot += direction
        print_warehouse(boxes, walls, robot)
    return boxes, robot

def calculate_sum(boxes:set) -> int:
    result = 0
    for box, typ  in boxes:
        if typ in ["O", "["]:
            gollum, row = box.real, box.imag
            result += row*100+gollum
    return int(result)




walls, boxes, robot = read_grid(grid)
print_warehouse(boxes, walls, robot)
boxes_after_move, robot = follow_move_order(move_order, walls, boxes, robot)
print_warehouse(boxes_after_move, walls, robot)
print("Part 1", calculate_sum(boxes_after_move))
