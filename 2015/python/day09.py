import re
import itertools

distances = {}
cities = set()
with open("inputs/2015/day09.txt") as f:
    for line in f.read().splitlines():
        city1, city2, distance = re.findall("([A-Za-z]{1,}) to ([A-Za-z]{1,}) = ([0-9]{1,})", line)[0]
        
        distances[(city1, city2)] = int(distance)
        cities.add(city1)
        cities.add(city2)

towntuples = list(itertools.permutations(cities))

minimal_distance = sum(distances.values())
maximal_distance = 0

for tt in towntuples:
    curr_dist = 0
    for index, city in enumerate(tt[:-1]):
        curr_dist += distances.get((city, tt[index+1]), distances.get((tt[index+1], city), 0))
    if curr_dist <= minimal_distance:
        minimal_distance = curr_dist
    if curr_dist >= maximal_distance:
        maximal_distance=curr_dist
    curr_dist=0

print(minimal_distance, maximal_distance)
        


