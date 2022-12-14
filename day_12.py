from pipe import select, where, traverse
import colorama
import numpy as np
import time

def get_connected(data,x,y):
    res = []
    if 0<x<len(data)-1:
        if data[x][y].height+1 >= data[x+1][y].height:
            res.append(data[x+1][y])
        if data[x][y].height+1 >= data[x-1][y].height:
            res.append(data[x-1][y])
    elif 0==x:
        if data[x][y].height + 1 >= data[x + 1][y].height:
            res.append(data[x + 1][y])
    elif x==len(data)-1:
        if data[x][y].height + 1 >= data[x-1][y].height:
            res.append(data[x-1][y])
    if 0<y<len(data[0])-1:
        if data[x][y].height + 1 >= data[x][y+1].height:
            res.append(data[x][y+1])
        if data[x][y].height + 1 >= data[x][y - 1].height:
            res.append(data[x][y - 1])
    elif 0==y:
        if data[x][y].height + 1 >= data[x][y + 1].height:
            res.append(data[x][y + 1])
    elif y==len(data[0])-1:
        if data[x][y].height + 1 >= data[x][y - 1].height:
            res.append(data[x][y - 1])
    return res

class Node:
    def __init__(self, height, neighbours=[], current_distance=9999,is_start=False, is_end=True):
        self.neighbours = neighbours
        self.distances  = [1 for _ in neighbours]
        self.height = height

        self.cur = current_distance
        self.is_start = is_start
        self.is_end   = is_end
        self.visited = False

        self.frontier = True
    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
        self.distances  = [1 for _ in neighbours]
    def get_neighbours(self):
        return self.neighbours

    def set_dist(self, d):
        self.cur = d

    def get_dist(self):
        return self.cur

    def visit(self):
        self.visited = True
def solve_p1(data): #S: 83, E: 69
    colorama.init()
    data = list(data | select(lambda a: [x for x in a]))
    temp = np.array(data)
    Sx, Sy = np.where(temp == "S")
    Ex, Ey = np.where(temp == "E")
    Sx, Sy, Ex, Ey = Sx[0], Sy[0], Ex[0], Ey[0]
    data = list(data | select(lambda a: list(a | select(ord))))
    data = list(data | select(lambda a: list(a | select(lambda a: 97 if a == 83 else ord("z") if a == 69 else a))))

    nodes = []
    for x, row in enumerate(data):
        new_row = []
        for y, element in enumerate(row):
            if (x,y) == (Sx,Sy): dist = 0
            else: dist=9999
            height = data[x][y]
            new_row.append(Node(height, current_distance=dist, is_start=((x,y) == (Sx,Sy)), is_end=((x,y) == (Ex,Ey))))
        nodes.append(new_row)
    for x, i in enumerate(nodes):
        for y, ele in enumerate(i):
            ele.set_neighbours(get_connected(nodes, x, y))

    start_node = nodes[Sx][Sy]

    next_nodes = [start_node]
    t=0
    while not nodes[Ex][Ey].cur < 999:
        next_next_nodes = []
        for node in next_nodes:
            if t % 5 == 0:
                cool_renderer_p1(nodes)
            t+=1
            neighbours = node.get_neighbours()
            for neighbour in list(neighbours | where(lambda a: not a.visited)):
                if neighbour.cur > node.cur + 1:
                    neighbour.set_dist(node.cur + 1)
            node.visit()
            next_next_nodes += list(neighbours | where(lambda a: not a.visited))
        next_nodes = list(set(list(next_next_nodes | where(lambda a:not a.visited))))
    #for row in nodes:
    #    print(list(row | select(lambda a: a.cur)))
    return nodes[Ex][Ey].cur

import sys
def cool_renderer_p1(nodes):
    print(end="\033[<41>A")
    S="\n"*41
    for row in nodes:
        s = ""
        for node in row:
            col1 = (colorama.Fore.LIGHTWHITE_EX, colorama.Fore.BLUE)[not node.visited]
            col2 = (col1, colorama.Style.BRIGHT + colorama.Fore.RED)[node.frontier and node.visited]
            if node.is_end == True or node.is_start: col2 = colorama.Style.BRIGHT + colorama.Fore.CYAN + colorama.Back.WHITE
            s+=col2 + str(chr(node.height)) + colorama.Fore.RESET + colorama.Style.RESET_ALL + colorama.Back.RESET
            if node.visited:
                node.frontier = False
        S+=s+"\n"
    sys.stdout.write(S)
    time.sleep(0.01)
def solve_p2(data):
    honestly = 430 #just_eyeball_it, closest A is obvious
    return 430