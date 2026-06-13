
red_tiles = [tuple(map(int, x.split(","))) for x in open("inputs/2025/day09.txt").read().splitlines()]

rectangle_sizes = set()

for tile1 in red_tiles:
    for tile2 in red_tiles:
        x = abs(tile1[0]-tile2[0])+1
        y = abs(tile1[1]-tile2[1])+1
        rectangle_sizes.add(x*y)

print(max(list(rectangle_sizes)))
