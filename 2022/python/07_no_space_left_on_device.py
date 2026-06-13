#!/usr/bin/env python

data = "input/day_07.txt"

with open(data) as f:
    commands = f.read().splitlines()
    
path=[]      
sizes={}
for cmd in commands:
    if "$ cd" in cmd:
        dir = cmd.split()[2]
        if dir == "/":
            path.append(dir)
        elif dir == "..":
            pwd = path.pop()
        else:
            path.append(f"{path[-1]}/{dir}")
    
    elif cmd[0].isdigit():
        for p in path:
            if p not in sizes.keys():
                sizes[p]=0
            sizes[p] += int(cmd.split()[0])

print(sum(s for s in sizes.values() if s<=100_000))
avail=70_000_000
used=avail-sizes["/"]
minimum=30_000_000
needed=minimum-used
print(min(s for s in sizes.values() if s >= needed))