import re 
import sympy
from sympy import Matrix, linsolve, symbols

data = open("inputs/2024/day13.txt").read().split("\n\n")

part1=0
part2=0

def solve_equation(buttonA, buttonB, prize):
    x, y = symbols("x, y")
    A = Matrix([[int(buttonA[0]), int(buttonB[0])], [int(buttonA[1]), int(buttonB[1])]])
    b = Matrix([int(prize[0]), int(prize[1])])
    return linsolve((A, b), [x, y])
    
for machine in data:
    buttonA = re.findall("Button A\: X\+([0-9]{1,})\, Y\+([0-9]{1,})\n", machine)[0]
    buttonB = re.findall("Button B\: X\+([0-9]{1,})\, Y\+([0-9]{1,})\n", machine)[0]
    
    prize =  re.findall("Prize\: X=([0-9]{1,})\, Y=([0-9]{1,})", machine)[0]
    
    # part 1
    for solA, solB in solve_equation(buttonA, buttonB, prize):
        if isinstance(solA, sympy.core.numbers.Integer) and isinstance(solB, sympy.core.numbers.Integer):
            part1 += (solA*3+solB)
            
    # part2
    prizeX = int(prize[0])+10000000000000
    prizeY = int(prize[1])+10000000000000
    
    for solA, solB in solve_equation(buttonA, buttonB, (prizeX, prizeY)):
        if isinstance(solA, sympy.core.numbers.Integer) and isinstance(solB, sympy.core.numbers.Integer):
            part2 += (solA*3+solB)

print("Part 1", part1)
print("Part 2", part2)
        
    