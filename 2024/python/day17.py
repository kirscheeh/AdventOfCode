import re
data = open("inputs/2024/day17.txt").read()

registers = {register:int(value) for register, value in re.findall("(A|B|C): ([0-9]{1,})", data)}
program = re.findall("([0-9]{1,})", re.findall("Program.*", data)[0])
output = []
instruction_pointer = 0

while instruction_pointer <= len(program)-1:
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer+1]
    
    literal_operand = int(operand)
    
    combo_operand = {"0": 0, "1":1, "2":2, "3":3, "4":registers.get("A"), "5":registers.get("B"), "6":registers.get("C"), "7": None}
    operand = combo_operand.get(operand)

    match opcode:
        case "0": # adv
            registers['A'] = registers['A']/(int(operand)**2)
        case "1": # bxl
            registers['B'] = registers['B'] ^ int(operand)
        case "2": #bst
            registers['B'] = operand % 8
        case "3": # jnz
            if registers.get("A") == 0:
                continue
            if not instruction_pointer == literal_operand:
                instruction_pointer = literal_operand
                continue
        case "4": #bxc
            registers['B'] = registers.get("B") ^ registers.get("C")
        case "5": # out
            print(operand)
            output.append(str(int(operand % 8)))
        case "6": # bdv
            registers['B'] = registers['A']/(int(operand)**2)
        case "7": # csv
            registers['C'] = registers['A']/(int(operand)**2)
    instruction_pointer += 2
    print(instruction_pointer, opcode, literal_operand, operand, registers, output)
    input()

print(output, registers)
