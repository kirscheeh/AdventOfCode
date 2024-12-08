from itertools import permutations
order, updates = open("inputs/2024/day05.txt").read().split("\n\n")

order =  [tuple(map(int, rule.split("|"))) for rule in order.splitlines() ]
updates = updates.splitlines()

helpdict = {}

for left, right in order:
    if not left in helpdict.keys():
        helpdict[left] = {'before':[], 'after':[]}
    if not right in helpdict.keys():
        helpdict[right] = {'before':[], 'after':[]}
    helpdict[left]['after'].append(right)
    helpdict[right]['before'].append(left)

def check_validity(input) -> bool:
    for index, rule in enumerate(input[1:]):
        if input[index] in helpdict[rule]['after']:
            return False 
    return True

def sort_quick_somehow(input) -> list:
    less = []
    equal = []
    greater = []

    if len(input) > 1:
        pivot = input[0]
        for elem in input:
            if elem in helpdict[pivot]['before']:
                less.append(elem)
            elif elem in helpdict[pivot]['after']:
                greater.append(elem)
            elif elem == pivot:
                equal.append(elem)
        return sort_quick_somehow(less)+equal+sort_quick_somehow(greater)
    else:
        return input

part1 = 0
part2 = 0

for update in updates:
    rules = list(map(int, update.split(",")))
    initially_correct=True
    corrected = rules.copy()
    if check_validity(rules):
        part1 += rules[int(len(rules)/2)]
    else:
        corrected = sort_quick_somehow(rules)
        part2 += corrected[int(len(corrected)/2)]

print("Part 1", part1)
print("Part 2", part2)
