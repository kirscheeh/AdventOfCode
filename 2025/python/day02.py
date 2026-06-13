import re

product_id_ranges = open("inputs/2025/day02.txt").read().splitlines()[0].split(",")

p1 = 0
p2=0

for id_range in product_id_ranges:
    start, stop = map(int, id_range.split("-"))
    
    for id in range(start, stop+1):
        
        number = str(id)
        
        if len(re.findall(r"^([0-9]{1,})\1$", number)) > 0:
            p1 += id
        if len(re.findall(r"^([0-9]{1,})\1{1,}$", number)) > 0:
            p2 += id
            
    
print(p1, p2)