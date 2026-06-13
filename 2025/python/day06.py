import re 
import math

data = open("inputs/2025/day06.txt").read().splitlines()

problems = {}

for line in data[:-1]:
   
    tmp = list(map(int, re.findall("[0-9]{1,}", line)))
    
    for index, number in enumerate(tmp):
        if not index in problems:
            problems[index] = []
        problems[index].append(number)

signs = re.findall("[+\-\*\/]", data[-1])

total = 0

for index, sign in enumerate(signs):
    match sign:
        case "+":
            total += sum(problems[index])
        case "*":
            total += math.prod(problems[index])
        case _ :
            print("Hello there!")


print("Part 1", total)
## part2

# well i hate cephalopod math