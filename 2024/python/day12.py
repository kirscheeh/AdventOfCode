import utils
from collections import deque

data = open("inputs/2024/day12.txt").read().splitlines()

grid = utils.input2complexdict(data)

start = 0+0j

def find_corners(positions) -> int:
    corner = 0
    for position in positions:
        # outer
        corner += position + (-1+0j) not in positions and position + (0-1j) not in positions
        corner += position + (1+0j) not in positions and position + (0-1j) not in positions
        corner += position + (-1+0j) not in positions and position + (0+1j) not in positions
        corner += position + (1+0j) not in positions and position + (0+1j) not in positions
        
        # inner
        corner += position + (-1+0j) in positions and position + (0-1j) in positions and position + (-1-1j) not in positions
        corner += position + (1+0j) in positions and position + (0-1j) in positions and position + (+1-1j) not in positions
        corner += position + (-1+0j) in positions and position + (0+1j) in positions and position + (-1+1j) not in positions
        corner += position + (1+0j) in positions and position + (0+1j) in positions and position + (+1+1j) not in positions
            
    return corner

def bfs(start, plant_type, grid):

    q = deque([start])
    visited = set()
    area, perimeter = 0,0
    while q:
        current_node = q.pop()
        if not current_node in visited:
            visited.add(current_node)
            area +=1
            
            for direction in [(1j), (-1j), (1+0j), (-1+0j)]:
                neighbour=current_node+direction
                if neighbour in grid.keys() and grid[neighbour] == plant_type:
                    if neighbour not in visited:
                        q.append(neighbour)
                else:
                    perimeter +=1 
    sites = find_corners(visited)

    return area, perimeter, sites, visited

visited_global = set()
total_price_perimeter = 0
total_price_sides = 0

for pos in grid:
    if pos not in visited_global:
        plant_type = grid[pos]
        area, perimeter, sides, visited = bfs(pos, plant_type, grid)
        visited_global.update(visited) 
         
        total_price_perimeter += area * perimeter
        total_price_sides += area * sides
        
print("Part1", total_price_perimeter)
print("Part2", total_price_sides)