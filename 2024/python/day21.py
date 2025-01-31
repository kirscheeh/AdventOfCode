data = open("inputs/2024/day21.txt").read().splitlines()

data = map(int, data)

def prune(secret):
    return secret % 16777216

def mix(secret, mixer):
    return secret ^ mixer 

def regenerate_secret(secret) -> int:
    new_secret = prune(mix(secret, secret * 64))
    new_secret = prune(mix(new_secret, int(new_secret/32)))
    new_secret = prune(mix(new_secret, new_secret*2048))
    return new_secret

part1 = 0
data = [123]
print(3)
for secret in data:
    for i in range(10):
        secret = regenerate_secret(secret)
        print(str(secret)[-1])
    part1 += secret


print("Part 1", part1)