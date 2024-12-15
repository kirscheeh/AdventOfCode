from collections import deque

data = open("inputs/2024/day11.txt").read().split()

def solve_naive(data, blinks): #works for p1
    for blink in range(blinks):
        mutator = []
        index = 0
        for stone in data:
            if stone == "0":
                mutator.append("1")
            elif len(stone) % 2 == 0:
                middle = len(stone)//2
                left, right = stone[:middle], stone[middle:].lstrip("0") or "0"
                mutator.append(left)
                mutator.append(right)
            else:
                mutator.append(str(int(stone)*2024))
            index += 1
        data = mutator
    print(len(data))

def solve_like_lanternfish(data, blinks):
    counter = {item: data.count(item) for item in data}

    for blink in range(blinks):
        new_counter = {item:0 for item in counter.keys()}
        new_counter["1"] = 0
        
        for item, value in counter.items():
            if item == "0":
                new_counter["1"] += value
            elif len(item) % 2 == 0:
                
                middle = len(item)//2
                left, right = item[:middle], item[middle:].lstrip("0") or "0"

                if not left in new_counter.keys():
                    new_counter[left] = 0
                if not right in new_counter.keys():
                    new_counter[right] = 0
                new_counter[left] += value 
                new_counter[right] += value 
            else:
                new_value = str(int(item)*2024)
                if not new_value in new_counter.keys():
                    new_counter[new_value] = 0
                new_counter[new_value] += value 
        
        counter = new_counter.copy()
    
    return sum(counter.values())


print("Part 1", solve_like_lanternfish(data, 25))
print("Part 2", solve_like_lanternfish(data, 75))
