from pipe import select, traverse
import numpy as np
#pylint: disable=no-value-for-parameter

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

    sorted_x = list(data | select(lambda x:x[0]))
    sorted_x.sort(key=lambda x: x[0])
    min_x_beacon = sorted_x[0]
    max_x_beacon = sorted_x[-1]

    min_x = min_x_beacon[0]
    max_x = max_x_beacon[0]

    min_x_index = list(data | select(lambda x:x[0])).index(min_x_beacon)
    max_x_index = list(data | select(lambda x:x[0])).index(max_x_beacon)

    max_x_data = data[max_x_index]
    min_x_data = data[min_x_index]

    max_x_dist = manhattan_dist(max_x_data[0], max_x_data[1])
    min_x_dist = manhattan_dist(min_x_data[0], min_x_data[1])

    target_row = int(input("target row: "))
    z=-1

    for x in range(min_x-min_x_dist, max_x+max_x_dist,1):
        point = [x, target_row]
        for sensor, beacon in data:
            dist = manhattan_dist(sensor, beacon)
            if manhattan_dist(point, sensor) <= dist:
                z+=1
                break

    return z

    

def solve_p2(data):
    data = list(data | select(lambda a: a.replace("Sensor at ", "").replace(" closest beacon is at ","").replace("y=","").replace("x=","")))
    data = list(data | select(lambda a: a.split(":")))
    data = list(data | select(lambda a: list(a | select(lambda b: b.split(",")))))
    data = list(data | select(lambda a: list(a | select(lambda b: list(b | select(int))))))
    # data = [[[Sx,Sy],[Bx,By]]]

    data = list(data | select(lambda a:[a[0], manhattan_dist(a[0], a[1])]))

    # i think i only need to check points that lie only m=1 diagonals of points

    beacons = list(data | select(lambda a: a[0]))
    lines = []
    upper = 4000000
    lower = 0
    for beacon in beacons:
        max_t = max(beacon[0], beacon[1])
        lines.append()

    return z
