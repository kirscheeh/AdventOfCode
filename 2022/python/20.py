#!/usr/bin/env python

from itertools import cycle

dec_key=1
dec_key = 811589153

rounds=1
rounds=10
inp = open("input/day_20.txt").read().splitlines()
inp = [int(x)*dec_key for x in inp]
zeroes = (inp.index(0), 0)

data = [tup for tup in enumerate(inp)]

cyc = cycle(data.copy())

lm = len(data)-1

for x in range(len(data)*rounds):
    curr = next(cyc)
    idx_old = data.index(curr)

    data.remove(curr)

    idx_new = (idx_old + curr[1] + lm) % lm
    data.insert(idx_new, curr)

idx_zero_tuple = data.index(zeroes)

print(sum([data[(idx_zero_tuple + i) % len(inp)][1]for i in [1000, 2000, 3000]]))
