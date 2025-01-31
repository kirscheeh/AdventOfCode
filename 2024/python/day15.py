grid, move_order = open("inputs/2024/day15.txt").read().split("\n\n")

walls = set()
boxes = []

print(grid)

for row, content in enumerate(grid.split()):
    for gollum, cell in enumerate(content):
        match cell:
            case "#": walls.add(gollum+1j*row)
            case "O": boxes.append(gollum+1j*row)
            case "@": robot = gollum+1j*row

for move in move_order:
    match move:
        case "^":
            if robot + (-1j) in walls:
                continue
            elif robot + (-1j) in boxes:
                box = robot + (-1j)
                while box + (-1j) in boxes and not box + (-1j) in walls:
                    box += (-1j)
            else:
                robot = robot + (-1j)
        case ">":
            if robot + (1+0j) in walls:
                continue
            elif robot + (1+0j) in boxes:
                pass
            else:
                robot = robot + (1+0j)
        case "v":
            if robot + (0+1j) in walls:
                continue
            elif robot + (0+1j) in boxes:
                pass
            else:
                robot = robot + (0+1j)
        case "<":
            if robot + (-1+0j) in walls:
                continue
            elif robot + (-1+0j) in boxes:
                pass
            else:
                robot = robot + (-1+0j)
