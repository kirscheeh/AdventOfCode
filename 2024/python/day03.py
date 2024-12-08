import re 
from math import prod 

memory = "".join(open("inputs/2024/day03.txt").read().splitlines())

part1=0
part2 = 0

enabled = True
for operation in re.finditer(re.compile(r"(mul\(([0-9]{1,3})\,([0-9]{1,3})\))|(don\'t|do)"), memory):
    match operation.group():
        case "don't":
            enabled = False 
        case "do":
            enabled=True
        case _:
            part1 += prod(map(int, re.findall("([0-9]{1,3})", operation.group())))

            if enabled:
                part2 += prod(map(int, re.findall("[0-9]{1,3}", operation.group())))

print("Part 1", part1)
print("Part 2", part2)