import re
from functools import cache

data = open("inputs/2024/day17.txt").read()

registers = {register:int(value) for register, value in re.findall("(A|B|C): ([0-9]{1,})", data)}
program = re.findall("([0-9]{1,})", re.findall("Program.*", data)[0])
output = []
instruction_pointer = 0

def get_combo_operand(operand:int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers.get("A")
        case 5:
            return registers.get("B")
        case 6:
            return registers.get("C")
        case 7:
            assert False
        
def operate(program:list, out:list, instruc_pointer:int):
    opcode = program[instruc_pointer]
    operand = int(program[instruc_pointer+1])
    match opcode:
        case "0": #adv
            registers['A'] = registers['A'] // (2**get_combo_operand(operand))
        case "1": #bxl
            registers['B'] = registers['B'] ^ operand 
        case "2": # bst
            registers['B'] = get_combo_operand(operand) % 8
        case "3": #jnz
            if registers.get("A") == 0:
                return out, instruc_pointer+2
            return out, operand
        case "4": # bxc
            registers['B'] = registers.get("B") ^ registers.get("C")
        case "5": # out
            out.append(str(get_combo_operand(operand)%8))
        case "6": # bdv
            registers['B'] = registers['A'] // (2**get_combo_operand(operand))
        case "7": # cdv
            registers['C'] = registers['A'] // (2**get_combo_operand(operand))
    return out, instruc_pointer+2
            
def run(program):
    instruction_pointer = 0
    out = []
    while instruction_pointer < len(program):
        out, instruction_pointer = operate(program, out, instruction_pointer)
        
    return ",".join(out)

print("Part 1", run(program))

@cache
def brute_force(a):
    registers['A'] = a
    registers['B'] = 0
    registers['C'] = 0
    instruction_pointer = 0
    out = []

    while instruction_pointer < len(program):
        out, instruction_pointer = operate(program, out, instruction_pointer)
        try:
            if out[0] != program[0]:
                return False
        except IndexError:
            pass
        if len(out) > len(program):
            return False
        elif len(out) == len(program):
            if out == program:
                return True
            else:
                return False

a=0
while not brute_force(a):
    a+=1
print("Part 2", a)
    
        




