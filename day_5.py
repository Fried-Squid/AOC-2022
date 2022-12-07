import numpy as np
def func(s):
    for a in range(0,len(s)-4):
        for b in range(4,len(s)):
            if s[a:b] == ['','','','']:
                s[a:b] = [""]
                return func(s)
    return s


def stackmove(n, s1, s2):
    for move in range(n):
        s2.append(s1.pop(-1))


def solve_p1(data):
    moves = list(map(lambda a: a.replace("move ", "").replace("from ", "").replace("to ", ""), data[10:]))
    moves = list(map(lambda a:list(map(int, a.split(" "))), moves))

    stacks = [a + [''] * (9 - len(a)) for a in list(map(func, list(map(lambda a: a.split(" "), data[0:8]))))]
    stacks = list(map(lambda a: list(filter(lambda x: x != '', a))[::-1], np.array(stacks).transpose().tolist()))

    print(stacks)
    for n,s1,s2 in moves:
        stackmove(n,stacks[s1-1],stacks[s2-1])

    result = "".join(list(map(lambda a:a[-1][1], stacks)))
    return result


def stackmove2(n, s1, s2):
    temp = s1[-1*n:]
    print(s1, temp, n)
    for move in range(n):
        s1.pop(-1)
        s2.append(temp[move])


def solve_p2(data):
    moves = list(map(lambda a: a.replace("move ", "").replace("from ", "").replace("to ", ""), data[10:]))
    moves = list(map(lambda a:list(map(int, a.split(" "))), moves))

    stacks = [a + [''] * (9 - len(a)) for a in list(map(func, list(map(lambda a: a.split(" "), data[0:8]))))]
    stacks = list(map(lambda a: list(filter(lambda x: x != '', a))[::-1], np.array(stacks).transpose().tolist()))

    print(stacks)
    for n,s1,s2 in moves:
        stackmove2(n,stacks[s1-1],stacks[s2-1])

    result = "".join(list(map(lambda a:a[-1][1], stacks)))
    return result

