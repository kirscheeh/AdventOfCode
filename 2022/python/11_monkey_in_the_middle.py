#!/usr/bin/env python

data = open("input/day_11.txt").read().split("\n\n")

import re
import sys

class Monkey:

    def __init__(self, items:list, operation:str, test:tuple):
        self.items=items 
        self.function=lambda old: eval(operation)
        self.divisor = test[0]
        self.true_monkey = test[1]
        self.false_monkey = test[2]
        self.inspected=0
        
    def inspect(self) -> None:
        elem = self.items[0]
        #print(f"Monkey inspects an item with a worry level of {elem}.")
        elem = self.function(elem)
        #print(f"Worry level is changed to {elem}.")
        elem = int(elem/3) # Part 1
        #elem = elem % 9699690 # Part 2
        self.items[0] = elem
        self.inspected+=1
        
    def keep_away(self) -> (int, int):
        elem = self.items[0]
        self.items = self.items[1:]
        if elem % self.divisor == 0: 
            #print(f"Item with worry level {elem} is thrown to monkey {self.true_monkey}.")
            return elem, self.true_monkey
        else:
            #print(f"Item with worry level {elem} is thrown to monkey {self.false_monkey}.")
            return elem, self.false_monkey
        
    def get_items(self):
        return self.items
    
    def add_item(self, item:int):
        self.items.append(item)
    
    def get_inspections(self):
        return self.inspected
    
    def get_divisor(self):
        return self.divisor
    
monkeys=[]

# prepare data for monkey class
for elem in data:
    elem = elem.split("\n")
    starting_items = re.findall("[0-9]{1,}", elem[1])
    items = list(map(int, starting_items))
    operation = re.findall("Operation: new = (.*)", elem[2])
    divisor = int(re.findall("[0-9]{1,}", elem[3])[0])
    receiver_true = int(re.findall("[0-9]{1,}", elem[4])[0])
    receiver_false=int(re.findall("[0-9]{1,}", elem[5])[0])
    
    monkeys.append(Monkey(items, operation[0], (divisor, receiver_true, receiver_false)))


# Part 2, get divisor
import numpy as np
divisors = np.prod([monk.get_divisor() for monk in monkeys])
print(divisors)

rounds=0
while rounds < 20:
    for monkey in monkeys:
        for index, _ in enumerate(monkey.get_items()):
            monkey.inspect()
            item, new_monk = monkey.keep_away()
            monkeys[new_monk].add_item(item)
            
    rounds+=1
 
active=[]   
for index, monkey in enumerate(monkeys):
    active.append(monkey.get_inspections())
    
active.sort()
print("Part", active[-2]*active[-1])



