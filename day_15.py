from pipe import select, chain, where
from itertools import combinations
#pylint: disable=no-value-for-parameter

def manhattan_dist(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return abs(x1-x2) + abs(y1-y2) #utterly buckwild

def solve_p1(data):
    return "solved"
    data = list(data | select(lambda a: a.replace("Sensor at ", "").replace(" closest beacon is at ","").replace("y=","").replace("x=","")))
    data = list(data | select(lambda a: a.split(":")))
    data = list(data | select(lambda a: list(a | select(lambda b: b.split(",")))))
    data = list(data | select(lambda a: list(a | select(lambda b: list(b | select(int))))))

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

def check_point(data, point):
    z=0
    for beacon,dist in data:
        if manhattan_dist(beacon,point) <= dist:
            return False
    return True

def solve_p2(data):
    print("start p2")
    data = list(data | select(lambda a: a.replace("Sensor at ", "").replace(" closest beacon is at ","").replace("y=","").replace("x=","")))
    data = list(data | select(lambda a: a.split(":")))
    data = list(data | select(lambda a: list(a | select(lambda b: b.split(",")))))
    data = list(data | select(lambda a: list(a | select(lambda b: list(b | select(int))))))
    data = list(data | select(lambda a:[a[0], manhattan_dist(a[0], a[1])]))

    upper = 4000000
    to_check = []
    for beacon, radius in data:
        radius += 1
        bx, by = beacon

        for i in range(0, radius):
            if 0 <= bx + radius - i <= upper and 0 <= by - i <= upper:
                to_check.append((bx + radius-i, by-i)) ## +bx - -
            if 0 <= bx - radius - i <= upper and 0 <= by + i <= upper:
                to_check.append((bx - radius+i, by+i)) ## -bx + +
            if 0 <= bx+i <= upper and 0 <= by + radius-i <= upper:
                to_check.append((bx+i, by + radius-i)) ## +by + -
            if 0 <= bx-i <= upper and 0 <= by - radius+i <= upper:
                to_check.append((bx-i, by - radius+i)) ## -by + -

    print(len(to_check))
    for each in to_check:
        x,y=each
        if check_point(data, each) and 0<=x<=upper and 0<=y<=upper:
            print(each)
            print(x*upper + y)

