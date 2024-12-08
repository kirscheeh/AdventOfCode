from operator import methodcaller
reports = [[*map(int, x.split())] for x in open("inputs/2024/day02.txt").read().splitlines()]


def check_safe(inp:list[int]) -> bool:
    if inp in [sorted(inp), sorted(inp, reverse=True)]:
        if set([abs(inp[i+1]-inp[i]) for i in range(len(inp)-1)]) <= {1, 2, 3}:
            return True 

    return False

def get_options(reports:list) -> list:
    one_removed=[]
    for report in reports:
        tmp = []
        for index in range(len(report)):
            tmp.append([lvl for i, lvl in enumerate(report) if i != index])
        one_removed.append(tmp+[report])
    return one_removed

print("Part 1", sum([check_safe(report) for report in reports]))   

print("Part 2", sum([sum([check_safe(option) for option in report_options]) >= 1 for report_options in get_options(reports)]))

            

