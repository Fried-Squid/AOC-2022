import importlib
from get import write_data


n = input(" Which day do you want to do? ")

try:
    n=str(int(n))
except ValueError:
    import datetime
    n = str(datetime.datetime.now().strftime("%d")).replace("0", "")

try:
    i = importlib.import_module(f'day_{n}')
except ModuleNotFoundError:
    x = write_data()
    if x:
        print(f'No day {n} found, successfully created day{n}.py and got the data as data/day{n}.txt')
        i = importlib.import_module(f'day_{n}')
    else:
        print(f'No day {n} found. Get script was unsucessful in creating the required files.')

    
with open(f'data/day{n}.txt', "r", encoding="utf-8") as f:
    data = f.read().split("\n")
    print(i.solve_p1(data))
    print(i.solve_p2(data))
