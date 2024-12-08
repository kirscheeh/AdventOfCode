import multiprocessing

data = open("inputs/2024/day06.txt").read().splitlines()

obstacles = []
visited = set()
positions = []

for row, content in enumerate(data):
    for gollum, element in enumerate(content):
        positions.append((row+1j*gollum))
        match element:
            case "#": obstacles.append((row+1j*gollum))
            case "^" | "v" | ">" | "<":
                direction = element 
                visited.add((row+1j*gollum))
                guard = row+1j*gollum
            case _: pass

initial_guard = guard
initial_direction = direction

def move(guard, direction, visited, obstacles):
    match direction:
        case "^":
            if guard-1-1j*0 in obstacles:
                direction = ">"
            else:
                guard = guard-1-1j*0
                visited.add(guard)
        case ">":
            if guard+0+1j*1 in obstacles:
                direction = "v"
            else:
                guard = guard-0+1j*1
                visited.add(guard)
        case "v":
            if guard+1-1j*0 in obstacles:
                direction = "<"
            else:
                guard = guard+1-1j*0
                visited.add(guard)
        case "<":
            if guard+0-1j*1 in obstacles:
                direction = "^"
            else:
                guard = guard-0-1j*1
                visited.add(guard)
    return guard, direction, visited

while guard in positions:
    guard, direction, visited = move(guard, direction, visited, obstacles)
    
visited.pop() # removes last entry that is not inside grid
print("Part 1", len(visited)) 

visited.remove(initial_guard) # here we cannot place obstacle

number_cycles = 0

def check_possibility(obstacles, guard, direction, visited) -> bool:
    instructions = set()
    while guard in positions:
        previous_instructions = instructions.copy()
        guard, direction, visited = move(guard, direction, visited, obstacles)
        instructions.add((guard, direction))

        if instructions == previous_instructions:
            return True
    return False

def check_quarter(input,  guard, direction, result):
    cycle=0
    for run, possibility in enumerate(input):
        tmp_obstacles = obstacles+[possibility]
        tmp_visited = set([initial_guard])
        cycle += check_possibility(tmp_obstacles, guard, direction, tmp_visited)
    result.append(cycle)
    return cycle

result = []
p1 = multiprocessing.Process(target=check_quarter, args=(list(visited)[::5], initial_guard, initial_direction, result))
p2 = multiprocessing.Process(target=check_quarter, args=(list(visited)[1::5], initial_guard, initial_direction, result))
p4 = multiprocessing.Process(target=check_quarter, args=(list(visited)[2::5], initial_guard, initial_direction, result))
p5 = multiprocessing.Process(target=check_quarter, args=(list(visited)[3::5], initial_guard, initial_direction, result))
p3 = multiprocessing.Process(target=check_quarter, args=(list(visited)[4::5], initial_guard, initial_direction, result))


p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()

print("Part 2", sum(result))  
# 640 630 640 
        