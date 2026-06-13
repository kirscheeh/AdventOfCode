import heapq 
from collections import defaultdict
from itertools import combinations

data = open("inputs/2024/day20.txt").read().splitlines()

paths = set()
for row, content in enumerate(data):
    for gollum, cell in enumerate(content):
        match cell:
            case "S":
                start = gollum+1j*row
                paths.add(start)
            case "E":
                end = gollum+1j*row
                paths.add(end)
            case ".":
                paths.add(gollum+1j*row)

def dijkstra(start, end, paths):
    distances = defaultdict(lambda: 1e9)
    distances[start] = 0

    pq = [(0, t:=0, start, [start])]

    while pq:
        current_distance, _, current_node, current_path = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for move in [(1+0j), (-1+0j), (0+1j), (0-1j)]:
            if (next_step:=current_node+move) in paths and (next_distance:=current_distance+1) < distances[next_step]:
                distances[next_step] = next_distance
                t +=1
                heapq.heappush(pq, (next_distance, t, next_step, current_path+[next_step]))

    return distances, current_path, len(current_path)-1

def check_possible_cheats(optimal_path, optimal_speed,paths): # brute force naive solution
    visited = set()
    results = defaultdict(lambda: 0)
    for current_position in optimal_path:
        for move in [(1+0j), (-1+0j), (0+1j), (0-1j)]:
            if not current_position+move in paths and current_position+2*move in paths:
                if current_position+move in visited:
                    continue
                visited.add(current_position+move)
                tmp_paths = paths.copy()
                tmp_paths.add(current_position+move)
                _, tmp_speed = dijkstra(start, end, tmp_paths)
                results[optimal_speed-tmp_speed]+=1
    return results

def check_cheats_clever(distances, cheat=2):
    part1=0
    part2=0
    for (coord1, dist1), (coord2, dist2) in combinations(distances.items(),2): # for each pair check the saved distance
        dist = abs((coord1-coord2).real) + abs((coord1-coord2).imag)
        if dist == 2:
            if dist2-dist1-dist >= 100: part1+=1
        if dist <= 20:
            if dist2-dist1-dist >= 100: part2+=1

    return part1, part2


distances, best_path, best_speed = dijkstra(start, end, paths)

print(check_cheats_clever(distances))
