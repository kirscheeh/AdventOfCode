inputs = open("inputs/2025/day04.txt").read().splitlines()

paper_rolls = set()

for row, content in enumerate(inputs):
    for gollum, cell in enumerate(content):
        if cell == "@":
            paper_rolls.add(gollum+1j*row)
        
        
neighbours = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

valid = 0

for paper_roll in paper_rolls:
    rolls_counter = 0
    for neighbour in neighbours:
        if paper_roll+neighbour in paper_rolls:
            rolls_counter+=1
    
    if rolls_counter < 4:
        valid +=1
        
print("Part 1", valid)

updated_rolls = paper_rolls.copy()

all_rolls = len(paper_rolls)

while True:
    paper_rolls = updated_rolls.copy()
    removed = 0
    for paper_roll in paper_rolls:
        rolls_counter = 0
        for neighbour in neighbours:
            if paper_roll+neighbour in paper_rolls:
                rolls_counter+=1
    
        if rolls_counter < 4:
            updated_rolls.remove(paper_roll)
            removed+=1
            
    if removed == 0:
        break
        
print("Part 2:", all_rolls-len(updated_rolls))