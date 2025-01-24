import heapq
data = open("/home/kirscheeh/repositories/AdventOfCode/inputs/2024/day09.txt").read().strip()

def decode_part1(data:str) -> list:
    fileID = 0
    disk = []
    for index, sign in enumerate(data):
        for i in range(int(sign)):
            if index % 2: # free space
                disk.append(".")
            else:
                disk.append(fileID)
        if not index % 2:
            fileID += 1
    return disk

def checksum(disk:list) -> int:
    result = 0
    for index, elem in enumerate(disk):
        if elem == ".":
            return result
        result = result + index*elem
    return result

def solve_part1(disk:list) -> list:
    for idx_block, elem in enumerate(disk[::-1]):
        if isinstance(elem, int):
            idx_free_space = disk.index(".")
            idx_block = len(disk) - idx_block -1
            if idx_free_space < idx_block:
                disk[idx_block], disk[idx_free_space] = disk[idx_free_space], disk[idx_block]
    return disk
print("Part 1", checksum(solve_part1(decode_part1(data))))

def decode_part2(data:str) -> dict:
    fileID = 0
    disk_blocks = {}
    free_spaces = {x:[] for x in range(0,10)}
    free_spaces2 = []
    index = 0
    for idx, sign in enumerate(data):
        if idx % 2: # free space
            heapq.heappush(free_spaces[int(sign)], index)
            heapq.heappush(free_spaces2, (index, -int(sign)))
        else:
            disk_blocks[fileID] = (index, int(sign))
            fileID += 1
        index += int(sign)

    return disk_blocks, free_spaces, free_spaces2

def checksum2(d):
    result = 0
    for fileID, (index, length) in d.items():
        for i in range(index, index+length):
            result = result + i*fileID

    return result

def printit(d):
    result = ["."]*100

    for fileID, (index, length) in d.items():
        for i in range(index, index+length):
            result[i] = str(fileID)
    print(result)

disk_blocks, free_spaces, free_spaces2 = decode_part2(data)
def try_t(disk_blocks):

    disk_blocks, free_spaces, free_spaces2 = decode_part2(data)
    disk_blocks2 = disk_blocks.copy()
    for fileID, (block_index, block_length) in dict(sorted(disk_blocks.items(), reverse=True)).items():
        free_spaces3 = []
        not_moved = True
        while free_spaces2:
            space_index, space_length = heapq.heappop(free_spaces2)
            if not_moved and abs(space_length) >= block_length and space_index < block_index:
                remaining_length = abs(space_length)-block_length

                disk_blocks[fileID] = (space_index, block_length)

                if remaining_length:
                    heapq.heappush(free_spaces3, (space_index+block_length, -remaining_length))
                not_moved = False
            else:
                heapq.heappush(free_spaces3, (space_index, space_length))
        free_spaces2 = free_spaces3.copy()
    print("Part 2", checksum2(disk_blocks))


try_t(disk_blocks)
