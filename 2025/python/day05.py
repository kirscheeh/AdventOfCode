import itertools

fresh_ranges, ids = open("inputs/2025/day05.txt").read().split("\n\n")

def check_range(ranges:list[tuple[int, int]], value:int) -> bool:
    for (start, stop) in ranges:
        if start <= value <= stop:
            return True
        
    return False

rngs = [tuple(map(int, rng.split("-"))) for rng in fresh_ranges.split("\n")]

ids = [int(i) for i in ids.split("\n")]

fresh = 0
for id in ids:
    fresh += check_range(rngs, id)
    
print("Part 1", fresh)

def connecting_intervals(rngs) -> list[tuple[int,int]]:
    
    new_range = rngs.copy()
    
    while True:
        rngs = list(new_range.copy())
        rngs = sorted(rngs, key=lambda x: x[0])
        new_range = []
        for index1, (start1, stop1) in enumerate(rngs):
            for index2 , (start2, stop2) in enumerate(rngs):
                
                if index2 <= index1:
                    continue
                
                if start1 <= start2 and stop2 <= stop1:
                    new_tuple = (start1, stop1)
                elif start1 <= start2 and stop1 < stop2 and start2 <= stop1:
                    new_tuple = (start1, stop2)
                else:
                    continue
                
                new_range = set([rng for (index, rng) in enumerate(rngs) if not index in [index1, index2]])
                new_range.add(new_tuple)
                
                break
            else:
                continue 
            break
        else:
            break     
    return rngs  
        
valid_intervals = connecting_intervals(rngs)
print("Part 2", sum([stop-start+1 for (start, stop) in valid_intervals]))
