from pipe import select,where, chain
import numpy as np
import time

def render(grid):
    print("""\n"""*140)
    print("----------")
    for row in grid:
        print("".join(list(row | select(lambda a: "." if a == 0.0 else a))))
    #time.sleep(0.2)

def render2(grid):
    pass

def sand_pos(grid, start):
    try:
        s = 0.0
        x, y = start
        while s == 0.0: #fail case= y+1, x !=, y+1, x-1 != 0.0
            s=grid[y+1][x]
            if s != 0.0:
                s=grid[y+1][x-1]
                if s == 0.0:
                    x-=1
            if s != 0.0:
                s=grid[y+1][x+1]
                if s == 0.0:
                    x += 1
            y+=1
        print((x,y,s))
        if grid[y][x-1] == 0.0:
            return [x-1,y]
        if grid[y][x+1] == 0.0:
            return [x+1,y]
        if grid[y-1][x] == 0.0:
            return [x,y-1]
    except IndexError:
        return None

def solve_p1(data):
    data = list(data | select(lambda a: a.split(" -> ")))
    data = list(data | select(lambda a: list(a | select(lambda b:list(b.split(",") | select(int))))))
    max_x = max(list(data | chain), key=lambda a: a[0])[0]
    max_y = max(list(data | chain), key=lambda a: a[1])[1]
    min_x = min(list(data | chain), key=lambda a: a[0])[0]
    min_y = 0 #500,0 is sand point

    data = list(data | select(lambda a: list(a | select(lambda b: [b[0]-min_x, b[1]-min_y]))))
    grid = np.zeros(((max_y-min_y)+1, (max_x-min_x)+1,)).tolist()
    print(len(grid), len(grid[0]))
    max_x = max(list(data | chain), key=lambda a: a[0])[0]
    max_y = max(list(data | chain), key=lambda a: a[1])[1]
    print(max_x, max_y)
    for scan in data:
        for index, point in enumerate(scan[:-1]):
            curr_x, curr_y = point[:]
            next_x, next_y = scan[index+1][:]
            line=[]

            if curr_x == next_x:
                if curr_y < next_y+1:
                    for i in range(curr_y, next_y+1):
                        line.append([curr_x, i])
                else:
                    for i in range(next_y, curr_y+1):
                        line.append([curr_x, i])
            if curr_y == next_y:
                if curr_x < next_x+1:
                    for i in range(curr_x, next_x+1):
                        line.append([i, curr_y])
                else:
                    for i in range(next_x, curr_x+1):
                        line.append([i, curr_y])

            print((curr_x, curr_y),(next_x,next_y))
            for x,y in line:
                print(x,y)
                grid[y][x] = "#"

    render(grid)
    test = 0
    sand_char = "o"
    start = [500-min_x,0]
    time.sleep(1)
    s=0
    while test is not None:
        test = sand_pos(grid, start)
        if test is not None:
            grid[test[1]][test[0]] = sand_char
            s+=1
        render(grid)
    return s

def solve_p2(data):
    print("part 2 start")
    data = list(data | select(lambda a: a.split(" -> ")))
    data = list(data | select(lambda a: list(a | select(lambda b: list(b.split(",") | select(int))))))
    max_y = max(list(data | chain), key=lambda a: a[1])[1]
    data.append([[-1000,max_y+2],[1000,max_y+2]])
    max_x = max(list(data | chain), key=lambda a: a[0])[0]
    max_y += 2
    min_x = min(list(data | chain), key=lambda a: a[0])[0]
    min_y = 0  # 500,0 is sand point

    data = list(data | select(lambda a: list(a | select(lambda b: [b[0] - min_x, b[1] - min_y]))))
    grid = np.zeros(((max_y - min_y) + 1, (max_x - min_x) + 1,)).tolist()

    max_x = max(list(data | chain), key=lambda a: a[0])[0]
    max_y = max(list(data | chain), key=lambda a: a[1])[1]

    for scan in data:
        for index, point in enumerate(scan[:-1]):
            curr_x, curr_y = point[:]
            next_x, next_y = scan[index + 1][:]
            line = []

            if curr_x == next_x:
                if curr_y < next_y + 1:
                    for i in range(curr_y, next_y + 1):
                        line.append([curr_x, i])
                else:
                    for i in range(next_y, curr_y + 1):
                        line.append([curr_x, i])
            if curr_y == next_y:
                if curr_x < next_x + 1:
                    for i in range(curr_x, next_x + 1):
                        line.append([i, curr_y])
                else:
                    for i in range(next_x, curr_x + 1):
                        line.append([i, curr_y])

            for x, y in line:
                grid[y][x] = "#"

    render2(grid)
    test = 0
    sand_char = "o"
    start = [500 - min_x, 0]
    time.sleep(1)
    while grid[start[1]][start[0]] != sand_char:
        test+=1
        y,x = sand_pos(grid, start)
        grid[x][y] = sand_char
        render2(grid)

    return test