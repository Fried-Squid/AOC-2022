from pipe import select, where
from functools import partial
import numpy as np

def get_connected(data,x,y):
    res = []
    if 0<x<len(data):
        res.append((data[x+1][y],(x+1,y)))
        res.append((data[x-1][y],(x-1,y)))
    elif 0<x:
        res.append((data[x-1][y],(x-1,y)))
    elif x<len(data):
        res.append((data[x+1][y],(x+1,y)))
    if 0<y<len(data[x]):
        res.append((data[x][y+1],(x,y+1)))
        res.append((data[x][y-1],(x,y-1)))
    elif 0<y:
        res.append((data[x][y-1],(x,y-1)))
    elif x<len(data[x]):
        res.append((data[x][y+1],(x,y+1)))
    return (x,y,data[x][y]), res

def solve_p1(data): #S: 83, E: 69
    data = list(data | select(lambda a: [x for x in a]))
    data = list(data | select(lambda a: list(a | select(ord))))
    data = list(data | select(lambda a: list(a | select(lambda a: "S" if a == 83 else "E" if a == 69 else a))))

    start,end=None,None #lol
    for i,each in enumerate(data):
        if "S" in each:
            start = (i,each.index("S"))
        elif "E" in each:
            end = (i,each.index("E"))
    
    Sx, Sy = start
    Ex, Ey = end

    
    data = list( data | select(lambda a: list(a | select(lambda b:(b,float('inf'))))))
    data = np.array(data)
    data[data == ["S",float('inf')]] = None

    visited = [([Sx, Sy],97, 0)]
    tentatative = [[get_connected(data,Sx, Sy),0]]
    print(tentatative)
    unvisited = data

    while len(unvisited[unvisited != None]) > 0:
        add_to_tentatative = []
        for ((Rx, Ry, Rh), connected_nodes), dist in tentatative: #[((0, 0, 'S'), [(97, (1, 0)), (97, (0, 1))]), 0]
            if Rh == 'S': Rh=97
            get_neighbours = partial(get_connected, unvisited)
            for Nh, (Nx, Ny) in connected_nodes:
                if Nh <= Rh+1:
                    visited.append(([Nx, Ny], Nh, dist+1))
                    add_to_tentatative += get_neighbours(Nx,Ny),dist #[[(Rx,Ry,Rh), [neighbours], dist?]]
                else:
                    pass


    print(tentatative)
    for row in data:
        print(row)
    