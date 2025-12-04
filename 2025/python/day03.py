import functools

joltage_banks = open("inputs/2025/day03.txt").read().splitlines()


@functools.cache
def recursive_joltages(bank:str, digits: int) -> int:
    
    if digits == 0:
        return 0
    
    if len(bank) == digits:
        return int(bank)
    
    keep = int(bank[0]) * 10 ** (digits-1) + recursive_joltages(bank[1:], digits-1)
  
    discard = recursive_joltages(bank[1:], digits)
    
    return max(keep, discard)

part1 = []
part2 = []

for bank in joltage_banks:
    part1.append(recursive_joltages(bank, 2))
    part2.append(recursive_joltages(bank, 12))
    
print(sum(part1), sum(part2))
    