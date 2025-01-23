import heapq
from collections import defaultdict

data = open("inputs/2024/day18.txt").read().splitlines()[:1024]
test = open("inputs/2024/day18.txt").read().splitlines()[1024:]


falling_bytes = [tuple(map(int, coord.split(","))) for coord in data]

paths = set() # (x,y)

for row in range(71):
    for gollum in range(71):
        if not (gollum, row) in falling_bytes:
            paths.add(gollum+1j*row)

def print_paths(x, y, bytes):
    for row in range(y):
        golcon = ""
        for gollum in range(x):
            if (gollum+1j*row) in bytes:
                golcon += "."
            else: 
                golcon +="#"
        print(golcon)

def dijkstra(start, end, paths):
    distances = defaultdict(lambda: 1e9)
    distances[start] = 0

    q = [(0, t:= 0, start)]

    while q:
        current_distance, _, current_position = heapq.heappop(q)

        if current_distance > distances[current_position]:
            continue 

        for direction in [(-1j), (1j), (1+0j), (-1+0j)]:
            next_position = current_position + direction

            if not next_position in paths:
                continue 

            next_distance = current_distance + 1 

            if next_distance < distances[next_position]:
                distances[next_position] = next_distance
                t+=1
                heapq.heappush(q, (next_distance, t, next_position))

    return distances[end]

print("Part 1", dijkstra((0+1j*0), (70+1j*70), paths))

for coord in test:
    x, y = tuple(map(int, coord.split(",")))
    paths.remove((x+1j*y))
    if dijkstra((0+1j*0), (70+1j*70), paths) == 1e9:
        print("Part 2", coord)
        break
    


