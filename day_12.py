from pipe import select, where
from functools import partial

def get_connected(data,x,y):
    try:
        a = data[x][y-1]
    except:
        a = None
    try:
        b = data[x][y+1]
    except:
        b = None
    try:
        c = data[x-1][y]
    except:
        c = None
    try:
        d = data[x+1][y]
    except:
        d = None

    return list([a,b,c,d] | where(lambda a:a is not None))
     

def solve_p1(data): #S: 83, E: 69
    data = list(data | select(lambda a: [x for x in a]))
    data = list(data | select(lambda a: list(a | select(ord))))
    data = list(data | select(lambda a: list(a | select(lambda a: "S" if a == 83 else "E" if a == 69 else a))))

    start,end=None,None #lol
    for i,each in enumerate(len(data)):
        if "S" in each:
            start = (i,each.index("S"))
        elif "E" in each:
            end = (i,each.index("E"))
    
    get_neighbours = partial(get_connected, data)
    Sx, Sy = start
    Ex, Ey = end

    
    

    for row in data:
        print(row)
    