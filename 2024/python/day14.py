
import re
import math
data = open("inputs/2024/day14.txt").read().splitlines()

positions = [re.findall("p=([0-9]{1,}),([0-9]{1,})", robot) for robot in data]
velocities = [re.findall("v=(\-?[0-9]{1,}),(\-?[0-9]{1,})", robot) for robot in data]

# transform to complex
for index in range(len(positions)):
    # positions
    x = int(positions[index][0][0])
    y = int(positions[index][0][1])
    positions[index] = x+1j*y
    #velocity
    x = int(velocities[index][0][0])
    y = int(velocities[index][0][1])
    velocities[index] = x+1j*y

positions1 = positions.copy()


def is_out_of_grid(position, max_x:int=11, max_y:int=7):
    x, y = position.real, position.imag
    return not (0 <= x < max_x and 0 <= y < max_y)

def teleport(position, x, y):
    x = position.real % x  # Wrap the x-coordinate
    y = position.imag % y  # Wrap the y-coordinate
    return complex(x, y)
    
def move(position, velocity, x:int=11, y:int=7) -> complex:
    if is_out_of_grid(position+velocity, x, y):
        new_position = teleport(position+velocity, x, y)
    else:
        new_position = position+velocity
    return new_position

def check_quadrants(x, y, robots) -> int:
    result = 0
    for row in range(y[0], y[1]):
        for gollum in range(x[0], x[1]):
            result += robots.count(gollum+1j*row)
    return result
            
def print_image(positions):
    with open("day14_image.txt", "w") as txt:
        for row in range(101):
            for gollum in range(103):
                if gollum+1j*row in positions:
                    txt.write("#")
                else:
                    txt.write(".")
            txt.write("\n")
def part1(positions):
    quadrants = [((0, 50), (0, 51)), ((51, 101), (0, 51)), ((0, 50),(52, 103)), ((51, 101), (52, 103))]

    for seconds in range(100):
        for index, (robot, velocity) in enumerate(zip(positions, velocities)):
            positions[index] = move(robot, velocity, x=101, y=103)
            
    total = []
    for quadrant in quadrants:
        total.append(check_quadrants(*quadrant, positions))
        
    print("Part 1", math.prod(total))

def part2(positions):
    iterator=1
    while True:
        for index, (robot, velocity) in enumerate(zip(positions, velocities)):
            positions[index] = move(robot, velocity, x=101, y=103)
        if len(set(positions)) == len(velocities):
            print("Part 2", iterator)
            print_image(positions)
            return
        iterator+=1
        
part1(positions)
part2(positions1)
        