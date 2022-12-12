from pipe import select, where
from functools import partial
import numpy as np

def get_connected(data,x,y):
    res = []
    if 0<x<len(data):
        res.append((x+1,y, data[x+1][y][0], data[x+1][y][1]))
        res.append((x-1,y, data[x-1][y][0], data[x-1][y][1]))
    elif 0<x:
        res.append((x+1,y, data[x+1][y][0], data[x+1][y][1]))
    elif x<len(data):
        res.append((x-1,y, data[x-1][y][0], data[x-1][y][1]))
    if 0<y<len(data[0]):
        res.append((x,y+1, data[x][y+1][0], data[x][y+1][1]))
        res.append((x,y-1, data[x][y-1][0], data[x][y-1][1]))
    elif 0<x:
        res.append((x,y+1, data[x][y+1][0], data[x][y+1][1]))
    elif x<len(data):
        res.append((x,y-1, data[x][y-1][0], data[x][y-1][1]))
    return [x,y,data[x][y][0],data[x][y][1]], res

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

    visited = []
    visited[0], tentatative = get_connected(data, Sx, Sy)
    unvisited = data.copy()

    while len(unvisited) > 0:
        for Tx,Ty,Th,Td in tentatative:
            Vx, Vy, Vh, Vd = Tx, Ty, Th, Td
            Rx, Ry, Rh, Rd = visited[0]
            if Rh+1 < Th:
                pass
            else:
                if Rd+1 >= Td:
                    pass
                else:
                    Vd = Rd+1
            visited.append(Vx, Vy, Vh, Vd)
            data[Vx][Vx] = [Vh,Vd]



    for row in data:
        print(row)
    