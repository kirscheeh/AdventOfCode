import utils
data = open("inputs/2024/day10.txt").read().splitlines()

grid = utils.input2complexdict(data)

hiking_starts = [key for key, val in grid.items() if val == "0"]
result = set()

def check_next_section(current_position, visited):
    global result
    if grid[current_position] == "9":
        result.add(current_position)
        return visited
    else:
        to_check = []
        for pos in [1, 1j, -1, -1j]:
            if current_position+pos not in visited and current_position+pos in grid.keys():
                if int(grid[current_position+pos]) == int(grid[current_position])+1:
                    to_check.append(current_position+pos)
        if len(to_check) > 0:
            return [check_next_section(possible, visited + [possible]) for possible in to_check]
        else: return 0

def flatten_to_tuples(data):
    result = []
    def extract_sequences(item):
        if isinstance(item, list):
            for sub_item in item:
                extract_sequences(sub_item)
        else:
            result.append(item)
    extract_sequences(data)
    return result 

endpoints = 0
hiking_trails = 0
for starting_point in hiking_starts:
    result = set()
    here = check_next_section(starting_point, [starting_point])
    endpoints += len(result)
    hiking_trails += flatten_to_tuples(here).count(starting_point)

print("Part 1", endpoints)
print("Part 2", hiking_trails)