def input2dict(puzzle:list[list[str]], to_int:bool=False) -> dict:
    result = {(x, y):0 for x,y in zip(range(len(puzzle)), range(len(puzzle[0])))}
    for row, content in enumerate(puzzle):
        for gollum, letter in enumerate(content):
            if to_int:
                tmp = int(letter)
            else:
                tmp = letter
            result[(row, gollum)] = tmp
    return result
            
def input2complexdict(puzzle):
    result = {x+1j*y:0 for x,y in zip(range(len(puzzle)), range(len(puzzle[0])))}
    for row, content in enumerate(puzzle):
        for gollum, letter in enumerate(content):
            result[gollum+1j*row] = letter
    return result
