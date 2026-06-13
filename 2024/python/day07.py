import re 
import math
import itertools 

data = open("inputs/2024/day07.txt").read().splitlines()
calibration = []

for line in data:
    result, *numbers = list(map(int, re.findall("[0-9]{1,}", line)))
    
    permutations = list(itertools.product(["+", "*", "||"], repeat=len(numbers)-1)) #part1 no ||
    for permutation in permutations:
        tmp = numbers[0]
        for index, sign in enumerate(permutation):
            match sign:
                case "+": tmp += numbers[index+1]
                case "*": tmp *= numbers[index+1]
                case "||": tmp = int(str(tmp)+str(numbers[index+1]))

        if tmp == result:
            calibration.append(result)
            break

print(sum(calibration))
