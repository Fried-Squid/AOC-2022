from pipe import select, where
from os import system

def measure_signal_strength(PC, X):
    if (PC+20) % 40 == 0:
        return PC * X
    else:
        return 0

def solve_p1(data):
    X  = 1
    PC = 1
    total = 0
    data = list(data | select(lambda a: "noop 0" if "noop" in a else a)
                     | select(lambda a: a.split(" "))
                     | select(lambda a: [a[0], int(a[1])]))
    for opcode, operand in data:
        if opcode == "noop":
            PC+=1
        elif opcode == "addx":
            PC+=1
            total += measure_signal_strength(PC, X)
            PC+=1
            X+=operand
        total += measure_signal_strength(PC, X)

    return total


def solve_p2(data):
    X   = 1
    PC  = 0
    screen = []
    data = list(data | select(lambda a: "noop 0" if "noop" in a else a)
                | select(lambda a: a.split(" "))
                | select(lambda a: [a[0], int(a[1])]))
    for opcode, operand in data:
        if opcode == "noop":
            if X - 1 <= PC%40 <= X + 1:
                screen.append("█")
            else:
                screen.append(" ")
            PC+=1
        elif opcode == "addx":
            if X-1 <= PC%40 <= X+1:
                screen.append("█")
            else:
                screen.append(" ")
            PC+=1
            if X-1 <= PC%40 <= X+1:
                screen.append("█")
            else:
                screen.append(" ")
            PC+=1
            X+=operand
    s=""
    for i in range(len(screen)):
        s+=screen[i]
        if (i+1) % 40 == 0:
            print(s)
            s=""