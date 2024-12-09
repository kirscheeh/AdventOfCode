import re
data = open("inputs/2024/day09.txt").read()

def decode(data):
    result = []
    block_number = 0
    for counter, sign in enumerate(data):
        if counter % 2 == 1:
            result.extend(["."*int(sign)])
        else:
            result.extend([str(block_number)]*int(sign))
            block_number += 1

    return list(result) 

def fill_blocks_recursively(data):
    if data.count(".") == 0:
        return data
    else:
        if data[-1] == ".":
            return fill_blocks(data[:-1])
        else:
            data[data.index(".")] = data[-1]
            return fill_blocks(data[:-1])

def fill_blocks_stupidly(data):
    while "." in data:
        if not data[-1] == ".":
            dot = data.index(".")
            data[dot] = data[-1]
        data = data[:-1]
    return data

def fill_blocks_fast(data):

    size_of_blocks = {block:data.count(block) for block in data if not set(block) == set(".") and not block == ""}
    blockIDs = list(map(str, sorted(list(map(int, size_of_blocks.keys())), reverse=True)))
    free_spaces = {index:len(x) for index, x in enumerate(data) if set(x) == set(".")}
    for blockID in blockIDs:
        for index, free_space_length in free_spaces.items():
            #print(blockID, index)
            remove=False
            if index >= data.index(blockID):
                break
            if free_space_length >= size_of_blocks[blockID] and index <= data.index(blockID):
                data = [x if x != blockID else "." for x in data]
                data = data[:index] + [blockID]*size_of_blocks[blockID] + ["."]*(free_space_length-size_of_blocks[blockID])+ data[index+1:]
                remove=True
                break 
        if remove:
            del free_spaces[index]

    return data


def add_empty_spaces(data, filled_data):
    return data + ["."]*(len(filled_data)-len(data))

def filesystem_checksum(data):
    data = [x for x in data if  x != ""]
    print(data)
    result = 0
    for index, fileID in enumerate(data):
        if fileID == ".":
            continue
        result += index*int(fileID)
    return result

decoded_data = decode(data)

#filled_data = fill_blocks(decoded_data)
#print("Part 1", filesystem_checksum(filled_data))

part2 = fill_blocks_fast(decoded_data)
print("Part 2", filesystem_checksum(part2))
