import re

def increase_straight_greater_three(pw:list[int]) -> bool:
    for index in range(len(pw)-2):
        if pw[index+2] - pw[index+1] == pw[index+1] - pw[index] == 1:
            return True
    return False


def no_mistaken_characters(pw:list[int]) -> bool:
    if 105 in pw or 111 in pw or 108 in pw:
        return False
    return True

def two_pairs(pw:list[int]) -> bool:
    txt = "-".join(map(str, pw))
    matches = re.findall(r"-([0-9]{2,3})-(\1)", txt)
    return len(matches) >= 2

def str_to_ascii_list(txt:str) -> list[int]:
    return [ord(c) for c in txt]

def ascii_list_to_str(inp: list[int]) -> str:
    return "".join([chr(i)for i in inp])

def increase(pw:list[int]) -> list[int]:
    pw_inv = pw[::-1]
    for index, elem in enumerate(pw_inv):
        if elem + 1 > 122:
            pw_inv[index] = 97
        else:
            pw_inv[index] += 1
            return pw_inv[::-1]

def generate_pw(inp:str, inc:bool=False) -> str:
    pw = str_to_ascii_list(inp)
    if inc:
        pw = increase(pw)
    while not (no_mistaken_characters(pw) and two_pairs(pw) and increase_straight_greater_three(pw)):
        pw = increase(pw)
    return ascii_list_to_str(pw)

old_pw = "hxbxwxba"
new_gen1 = generate_pw(old_pw)
print("Part 1", new_gen1)
new_gen2 = generate_pw(new_gen1, True)
print("Part 2", new_gen2)