import importlib

n = "7"
i = importlib.import_module(f'day_{n}')
with open(f'data/day{n}.txt', "r") as f:
    data = f.read().split("\n")
    print(i.solve_p1(data))
    print(i.solve_p2(data))