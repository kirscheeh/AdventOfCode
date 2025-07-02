import math

def get_divisors(number: int) -> set[int]:
    result = set()
    for i in range(1, int(math.isqrt(number)) + 1):
        if number % i == 0:
            result.add(i)
            result.add(number // i)
    return result

inp = 36000000
house = 154675*2

while not (x:=sum(get_divisors(house))*10) >= inp:
    house+=1
    
print(house)