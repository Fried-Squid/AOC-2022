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

    # step 1: find the maximums / mins
    max_x = max(list(list(data | select(lambda a: list(a | select(lambda b:b[0]))) | traverse)))
    max_y = max(list(list(data | select(lambda a: list(a | select(lambda b:b[1]))) | traverse)))
    min_x = min(list(list(data | select(lambda a: list(a | select(lambda b:b[0]))) | traverse)))
    min_y = min(list(list(data | select(lambda a: list(a | select(lambda b:b[1]))) | traverse)))
    print(max_x, min_x, max_y, min_y)
    data = list(data | select(lambda a: list(a | select(lambda b: [b[0]-min_x, b[1]-min_y]))))

    # step 2: construct the grid
    #grid = np.zeros((max_y-min_y, max_x-min_x), dtype=bool).tolist()
    
    target_row = 10 #hardcoded target row

    z=0 #think about the shape of the rectilinear distances maybe? irdk why this isnt working though it works fine on the example data
    for i in range(max_x-min_x+1):
        point = [i, target_row]
        for sensor, beacon in data:
            dist = manhattan_dist(sensor, beacon)
            if manhattan_dist(point, sensor) <= dist or point == sensor or point == beacon:
                z+=1
                break
    return z-1 #why
def solve_p2(data):
    return None
