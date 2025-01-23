from collections import deque
from functools import cache
import heapq

data = open("inputs/2024/day16.txt").read().splitlines()

paths = set()

for row, content in enumerate(data):
    for gollum, cell in enumerate(content):
        match cell:
            case "S":
                start = gollum+1j*row 
                start = (gollum, row)
                paths.add(start)
            case "E":
                end = gollum+1j*row
                end = (gollum, row)
                paths.add(end)
            case ".":
                paths.add((gollum, row))
                #paths.add(gollum+1j*row)

def dijkstra(start, end, paths):
    distances = {node: float('inf') for node in paths}
    distances[start] = 0
    
    pq = [(0, start, ">")]


    while pq:
        current_distance, current_node, current_facing = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue  # not shortest path anymore

        for next_position, facing in zip([(current_node[0]-1, current_node[1]), (current_node[0]+1, current_node[1]), (current_node[0], current_node[1]+1), (current_node[0], current_node[1]-1)], ["<", ">", "v", "^"]):
            if not next_position in paths:
                continue

            if not facing == current_facing:
                distance = current_distance + 1001
            else:
                distance = current_distance + 1

            if distance < distances[next_position]:
                distances[next_position] = distance
                heapq.heappush(pq, (distance, next_position, facing))


    return distances[end]

dist = dijkstra(start, end, frozenset(paths))
print("Part 1", dist)
