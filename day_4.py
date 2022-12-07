def solve_p1(data):
    data = list(map(lambda a: a.split(","), data))
    data = list(map(lambda a: list(map(lambda b: b.split("-"), a)), data))
    data = list(map(lambda a: list(map(lambda b: list(map(int, b)), a)), data))
    data = list(map(lambda a: list(map(lambda b: list(range(b[0], b[1]+1)), a)), data))
    data = list(map(lambda a: all([x in a[1] for x in a[0]]) or all([x in a[0] for x in a[1]]), data))
    return sum(data)


def solve_p2(data):
    data = list(map(lambda a: a.split(","), data))
    data = list(map(lambda a: list(map(lambda b: b.split("-"), a)), data))
    data = list(map(lambda a: list(map(lambda b: list(map(int, b)), a)), data))
    data = list(map(lambda a: list(map(lambda b: list(range(b[0], b[1]+1)), a)), data))
    data = list(map(lambda a: any([x in a[1] for x in a[0]]) or any([x in a[0] for x in a[1]]), data))
    return sum(data)

