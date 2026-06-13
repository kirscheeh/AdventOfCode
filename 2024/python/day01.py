data = [*map(int, open('inputs/2024/day01.txt').read().split())]

left, right = sorted(data[0::2]), sorted(data[1::2])

print("Part 1", sum([abs(x-y) for x,y in zip(left, right)]))
print("Part 2", sum([x*right.count(x) for x in left]))
