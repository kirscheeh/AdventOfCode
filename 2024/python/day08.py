import itertools
import utils

data = open("inputs/2024/day08.txt").read().splitlines()

grid = utils.input2complexdict(data)

d = {}
antennas = []
for row, content in enumerate(data):
    for gollum, item in enumerate(content):
        if item.isdigit() or item.isalpha():
            if not item in d.keys():
                d[item] = []
            d[item].append(row+1j*gollum)
            antennas.append(row+1j*gollum)
        else:
            pass

part1= set()
part2= set()

for antenna, positions in d.items():
    pairs = itertools.permutations(positions, 2)
    for one, two in pairs:
        distance = two-one
        for tmp, mathy in zip([two+distance, one-distance], ['+', '-']):
            part1.append(tmp)
            while tmp in grid.keys():
                if not tmp in antennas:
                    part2.add(tmp)
                match mathy:
                    case "+":
                        tmp += distance
                    case "-":
                        tmp -= distance
                


print("Part 1", len([antinode for antinode in part1 if antinode in grid.keys()])+)
print("Part 2", len([antinode for antinode in part2 if antinode in grid.keys()])+len(antennas))