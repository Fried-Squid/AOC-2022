from pipe import select, traverse
import numpy as np

def manhattan_dist(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return abs(x1-x2) + abs(y1-y2) #utterly buckwild

def solve_p1(data):
    data = list(data | select(lambda a: a.replace("Sensor at ", "").replace(" closest beacon is at ","").replace("y=","").replace("x=","")))
    data = list(data | select(lambda a: a.split(":")))
    data = list(data | select(lambda a: list(a | select(lambda b: b.split(",")))))
    data = list(data | select(lambda a: list(a | select(lambda b: list(b | select(int))))))
    # data = [[[Sx,Sy],[Bx,By]]]

    # step 1: find the maximums
    max_x = max(list(list(data | select(lambda a: list(a | select(lambda b:b[0]))) | traverse)))
    max_y = max(list(list(data | select(lambda a: list(a | select(lambda b:b[1]))) | traverse)))

    # step 2: construct the grid
    grid = np.zeros((max_x, max_y)).tolist()
    
def solve_p2(data):
    return None
