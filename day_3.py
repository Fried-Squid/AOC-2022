def reverse_case(char: str) -> str:
    if char.upper() == char:
        return char.lower()
    else:
        return char.upper()


def solve_p1(data):
    data = list(map(lambda x: "".join(list(map(lambda a: reverse_case(a), x))), data))
    data = list(map(lambda a: [a[0:len(a)//2], a[len(a)//2:]], data))
    data = list(map(lambda a: list(filter(lambda b: b in a[1], a[0]))[0], data))
    data = list(map(lambda a: ord(a)-64 if a == a.upper() else ord(a)-70, data))
    return sum(data)


def solve_p2(data):
    data = list(map(lambda x: "".join(list(map(lambda a: reverse_case(a), x))), data))
    data = zip(*(iter(data),) * 3)
    data = list(map(lambda a: [list(filter(lambda b: b in a[1], a[0])), a[2]], data))
    data = list(map(lambda a:  list(filter(lambda b: b in a[1], a[0]))[0], data))
    data = list(map(lambda a: ord(a)-64 if a == a.upper() else ord(a)-70, data))
    return sum(data)