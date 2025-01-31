from collections import defaultdict, deque
import re
inputs, logic = open("inputs/2024/day24.txt").read().split("\n\n")
operators = {"AND":"&", "XOR":"^", "OR":"|"}
values = defaultdict(lambda:0)

for inp in inputs.splitlines():
    gate, value = re.findall("([xyz][0-9]{1,2})\: ([0-9]{1,})", inp)[0]
    values[gate] = int(value)

zetts = set()
unsolved = set()  
for operation in logic.splitlines():
    first, operator, second, result = re.findall("([0-9a-zA-Z]{3}) (AND|OR|XOR) ([0-9a-zA-Z]{3}) -> ([0-9a-zA-Z]{3})", operation)[0]
    for tmp in [first, second, result]:
        if tmp.startswith("z"):
            zetts.add(tmp)
    if first in values and second in values:
        values[result] = eval(f"{values[first]} {operators[operator]} {values[second]}")
    else:
        unsolved.add((first, operator, second, result))
 
q = deque(unsolved)       
while q:
    for zett in zetts:
        if not zett in values:
            break 
    else:
        break
    (first, operator, second, result) = q.pop()
    
    if first in values and second in values:
        values[result] = eval(f"{values[first]} {operators[operator]} {values[second]}")
    else:
        q.appendleft((first, operator, second, result))

zetts = sorted(list(zetts), reverse=True)  
binary_number=""   
for zett in zetts:
    
    binary_number += str(values[zett])

print("Part 1", int(binary_number, 2))