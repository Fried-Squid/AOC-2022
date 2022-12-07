from itertools import groupby


def solve_p1(data):
    data = [sum(list(map(lambda a:int(a), x))) for x in [list(group) for k, group in groupby(data, lambda x: x == "") if not k]]
    return max(data)


def solve_p2(data):
    data = [sum(list(map(lambda a:int(a), x))) for x in [list(group) for k, group in groupby(data, lambda x: x == "") if not k]]
    return sum(sorted(data, reverse=True)[0:3])
