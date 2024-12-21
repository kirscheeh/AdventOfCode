import re
from collections import defaultdict

data = open("inputs/2024/day09.txt").read()

def decode(data):
    result = []
    block_number = 0
    for counter, sign in enumerate(data):
        print(counter)
        if counter % 2 == 1:
            if not int(sign) == 0:
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
            return fill_blocks_recursively(data[:-1])
        else:
            data[data.index(".")] = data[-1]
            return fill_blocks_recursively(data[:-1])

def fill_blocks_stupidly(data):
    while "." in data:
        if not data[-1] == ".":
            dot = data.index(".")
            data[dot] = data[-1]
        data = data[:-1]
    return data

def fill_blocks_fast(data):

    size_of_blocks = defaultdict(int)
    
    for block in data:
        if block.isdigit():
            size_of_blocks[block] +=1

    size_of_blocks = dict(sorted(size_of_blocks.items(), key=lambda item: int(item[0]), reverse=True))

    lengths_of_free_space = [len(item) for item in data if not item.isdigit()]

    for blockID, block_length in size_of_blocks.items():
        if block_length > max(lengths_of_free_space):
            continue
        for index, item in enumerate(data):
            print(blockID, index)
            if not item.isdigit():
                starting_index = data.index(blockID)
                if len(item) >= block_length and index <= starting_index:
                    # replace old block by .
                    stop_index = starting_index+block_length
                    data[starting_index] = "."*block_length

                    data = data[:starting_index+1] + data[stop_index:]

                    if not len(item) == block_length:
                        data = data[:index] + [str(blockID)]*block_length + ["."*(len(item)-block_length)] + data[index+1:]
                    else: 
                        data = data[:index] + [str(blockID)]*block_length + data[index+1:]
                    lengths_of_free_space.remove(len(item))
                    break
                elif index > starting_index:
                    break

    return "".join(data)
  

def add_empty_spaces(data, filled_data):
    return data + ["."]*(len(filled_data)-len(data))

def filesystem_checksum(data):

    data = [x for x in data if  x != ""]
    result = 0
    for index, fileID in enumerate(data):
        if fileID == ".":
            continue
        result += index*int(fileID)
    return result

decoded_data = decode(data)
print("Hello")

#filled_data = fill_blocks(decoded_data)
#print("Part 1", filesystem_checksum(filled_data))

part2 = fill_blocks_fast(decoded_data)

print("Part 2", filesystem_checksum(part2))
