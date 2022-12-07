def solve_p1(data, n=4):
    s = data[0]
    return list(map(lambda a: len(set(a)), [s[a:a+n] for a in range(len(s)-n)])).index(n)+n


def solve_p2(data):
    return solve_p1(data, 14)