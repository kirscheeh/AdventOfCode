
rotations = open('inputs/2025/day01.txt').read().splitlines()

position = 50

crossed_zero=0
is_zero = 0

for rotation in rotations:
    direction, steps = rotation[0], int(rotation[1:])
        
    match direction:
        case "L":
            for step in range(1, steps+1):
                position -= 1
                
                if position == -1:
                    position = 99
                    
                if position == 0:
                    crossed_zero+=1

        case "R":
            for step in range(1, steps+1):
                position += 1
                
                if position == 100:
                    position = 0

                    crossed_zero+=1
    if position == 0:
        is_zero+=1
                    

print("Part 1:", is_zero)
print("Part 2:", crossed_zero)


