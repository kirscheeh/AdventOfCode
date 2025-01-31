
data = open("inputs/2024/day25.txt").read().split("\n\n")

keys = []
locks = []

def translate_lock(elem):
    elem = elem.splitlines()
    columns = [0]*len(elem[0])

    for rowcontent in elem[1:]:
        for gollum, cell in enumerate(rowcontent):
            columns[gollum] += cell == "#"
    return columns


def translate_key(elem):
    elem = elem.splitlines()
    columns = [0]*len(elem[0])
    elem = elem[::-1]

    for rowcontent in elem[1:]:
        for gollum, cell in enumerate(rowcontent):
            columns[gollum] += cell == "#"
    return columns

for elem in data:
    if set(elem[0]) == set("#"):
        locks.append(translate_lock(elem))
    else:
        keys.append(translate_key(elem))

fits = 0
for lock in locks:
    for key in keys:
        fits += sum([lock[i]+key[i]>5 for i in range(len(key))]) == 0
            
print(fits)