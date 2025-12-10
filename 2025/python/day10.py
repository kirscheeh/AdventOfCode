import re 
import itertools

manual = open("inputs/2025/day10.txt").read().splitlines()

def process_buttons(buttons: list[str]) -> list[tuple[int, int]]:
    tuples = []
    for button in buttons:
        tuples.append(tuple(map(int, re.findall("([0-9]{1,})", button))))
    return tuples

def process_joltage(joltages: str) -> list[int]:
    return list(map(int, re.findall("([0-9]{1,})", joltages)))

all_button_presses=0

for machine in manual:
    indicator_light_diagram, *remainder = machine.split(" ", 1)
    *button_wiring_schematics, joltage_requirements = remainder[0].split(" ")
  
    indicator_light_diagram = indicator_light_diagram[1:-1]
    button_wiring_schematics = process_buttons(button_wiring_schematics)
    joltage_requirements = process_joltage(joltage_requirements)
    print(joltage_requirements)
    # powerset
    button_combinations = itertools.chain.from_iterable(itertools.combinations(button_wiring_schematics, r) for r in range(len(button_wiring_schematics)+1))

    button_combinations = sorted(button_combinations, key = lambda x: len(x)) # part1
    
    # part 1
    for buttons in button_combinations:
        light = ["."]*len(indicator_light_diagram)
        
        butts_to_press = list(map(int, re.findall("[0-9]{1,}", str(buttons))))
        
        for butt in butts_to_press:
            # Part 1

            if light[butt] == "#":
                light[butt] = "."
            else:
                light[butt] = "#"
        
        if "".join(light) == indicator_light_diagram:
            all_button_presses += len(buttons)
            break
    
    # part 2
    joltages = [0]*len(joltage_requirements)
    str_joltage_requirements = "".join([str(x) for x in joltage_requirements])
    
    print(joltages)
    
    button_presses=1
    while not "".join(str(x) for x in joltages) == str_joltage_requirements:
        joltages = [0]*len(joltage_requirements)
        button_combinations = itertools.combinations_with_replacement(button_wiring_schematics, button_presses)

        for bt in button_combinations:
        
            butts_to_press = list(map(int, re.findall("[0-9]{1,}", str(bt))))
            for butt in butts_to_press:
                joltages[butt] +=1
        print(joltage_requirements, joltages)
        input()
        button_presses +=1
                     
   
        
print("Part 1", all_button_presses)