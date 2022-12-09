global U,D,L,R
U,L,D,R = [0,1], [-1,0], [0,-1], [1,0]
NW,SW,NE,SE = [1,-1],[-1,-1],[1,1],[-1,1]

def dist(v1,v2):
    x1,y1 = v1
    x2,y2 = v2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def is_touching(head_pos,tail_pos):
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos
    diff_x, diff_y = abs(head_x-tail_x),abs(head_y-tail_y)
    if diff_x <= 1 and diff_y <=1:
        return True, (head_x-tail_x, head_y-tail_y)
    else:
        return False,(head_x-tail_x, head_y-tail_y)

def solve_p1(data):
    global U,D,L,R,NW,SW,SE,NE
    head_pos = [0,0]
    tail_pos = [0,0]
    tail_visits = [[0,0]]
    vec_add = lambda a,b: [a[i] + b[i] for i in range(2)]

    data = list(map(lambda a:a.split(" "), data))
    directiondict = {"U":U[:], "D":D[:], "L":L[:], "R":R[:]}
    for direction, mag in data:
        mag=int(mag)
        direction = directiondict[direction]
        for i in range(mag):
            head_pos = vec_add(head_pos, direction)
            touching = is_touching(head_pos, tail_pos)
            #rel_pos = vec_add(vec_add(head_pos, [-x for x in tail_pos]),[2,2])
            #print(touching[0])
            if not touching[0]:
                possible_direction = U[:],L[:],D[:],R[:],NW[:],SW[:],NE[:],SE[:]
                possible_direction = list(map(lambda a:vec_add(tail_pos, a), possible_direction))
                possible_direction = list(map(lambda a:dist(a, head_pos), possible_direction))
                tail_dir = (U[:],L[:],D[:],R[:],NW[:],SW[:],NE[:],SE[:])[possible_direction.index(min(possible_direction))]
                tail_pos = vec_add(tail_pos, tail_dir)
            rel_pos = vec_add(vec_add(head_pos, [-x for x in tail_pos]), [1,1])
            if tail_pos not in tail_visits:
                tail_visits.append(tail_pos)
    #print(tail_visits)
    return len(tail_visits)


def tailmove(head_pos, tail_pos):
    global U,D,L,R,NW,SW,SE,NE
    vec_add = lambda a,b: [a[i] + b[i] for i in range(2)]
    touching = is_touching(head_pos, tail_pos)
    if not touching[0]:
        possible_direction = U[:],L[:],D[:],R[:],NW[:],SW[:],NE[:],SE[:]
        possible_direction = list(map(lambda a:vec_add(tail_pos, a), possible_direction))
        possible_direction = list(map(lambda a:dist(a, head_pos), possible_direction))
        tail_dir = (U[:],L[:],D[:],R[:],NW[:],SW[:],NE[:],SE[:])[possible_direction.index(min(possible_direction))]
        tail_pos = vec_add(tail_pos, tail_dir)
    return head_pos, tail_pos

def solve_p2(data):
    global U,D,L,R,NW,SW,SE,NE
    pos_list =  [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    tail_visits = [[0,0]]
    
    vec_add = lambda a,b: [a[i] + b[i] for i in range(2)]
    data = list(map(lambda a:a.split(" "), data))
    directiondict = {"U":U[:], "D":D[:], "L":L[:], "R":R[:]}


    for direction, mag in data:
        mag=int(mag)
        direction = directiondict[direction]
        for i in range(mag):
            pos_list[0] = vec_add(pos_list[0], direction)
            for i in range(1,len(pos_list)):
                pos_list[i-1], pos_list[i] = tailmove(pos_list[i-1], pos_list[i])

            if pos_list[-1] not in tail_visits:
                tail_visits.append(pos_list[-1])
    print(tail_visits)
    return len(tail_visits)