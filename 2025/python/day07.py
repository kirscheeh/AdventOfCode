
from functools import lru_cache

data = open("inputs/2025/day07.txt").read().splitlines()

grid = {}

origin_tachycon_beam = 0
splitters = set()
for row, content in enumerate(data):
    for gollum, cell in enumerate(content):
        grid[gollum+1j*row] = cell

        if cell == "S":
            origin_tachycon_beam = gollum+1j*row

        if cell == "^":
            splitters.add(gollum+1j*row)

def exit_manifold(beam_pos, hit_splitters, used_beams):

    if beam_pos in used_beams:
        return hit_splitters
    
    used_beams.add(beam_pos)

    if beam_pos not in grid:
        return hit_splitters
    
    if beam_pos in splitters:
        hit_splitters.add(beam_pos)
        return exit_manifold(beam_pos+(-1+1j), hit_splitters.copy(), used_beams) | exit_manifold(beam_pos+(1+1j), hit_splitters.copy(), used_beams)
    else:
        return exit_manifold(beam_pos+(1j), hit_splitters.copy(), used_beams)
    
@lru_cache # works, but too inefficient for real input
def quantum_tachyon(beam_pos, path):
    if beam_pos not in grid:
        return [path]
    
    results = []
    if beam_pos in splitters:
        results += quantum_tachyon(beam_pos+(-1+1j), path + (beam_pos,))
        results += quantum_tachyon(beam_pos+(+1+1j), path + (beam_pos,))
    else:
        results += quantum_tachyon(beam_pos+(1j), path + (beam_pos,))

    return results
    
print("Part 1", len(exit_manifold(origin_tachycon_beam, set(), used_beams=set())))
# print("Part 2", len(quantum_tachyon(origin_tachycon_beam, tuple())))