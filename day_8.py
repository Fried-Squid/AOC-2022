#This day went awful, 3 hours used.
#Gotta be careful with edge cases in future, avoid tunnell vision too.
#Oh well. Ill do better tomorrow
# ~Ace

#pylint: disable=consider-using-enumerate
#pylint: disable=missing-function-docstring
#pylint: disable=invalid-name
#pylint: disable=line-too-long

def get_fullrows(parent,i,j):
    parentT = [list(map(lambda a:a[i], parent)) for i in range(len(parent[0]))]
    return list(map(lambda a:[x[0] for x in a] if len(a)>=1 else [], [parent[i][0:j][::-1], parent[i][j+1:],parentT[j][0:i][::-1], parentT[j][i+1:]]))


def check_vis(data,i,j):
    tree=data[i][j]
    ranges = list(map(lambda a:tree[0]>max(a) if len(a)>=1 else 0, get_fullrows(data,i,j)))

    if any(ranges):
        return True
    else:
        return False


def solve_p1(data):
    data   = [[int(y) for y in x] for x in data]
    data[0] = list(zip(data[0],[1 for i in range(len(data[0]))]))
    data[-1] = list(zip(data[-1],[1 for i in range(len(data[-1]))]))
    data[1:-1] = [[(x, 1 if i==0 or i==len(a)-1 else 0) for i,x in enumerate(a)] for a in data[1:-1]]


    for _ in range(2):
        inner_data = [a[1:-1] for a in data[1:-1]]
        for i in range(len(inner_data)):
            for j in range(len(inner_data[i])):
                is_visible = check_vis(data,i+1,j+1)
                data[i+1][j+1] = (data[i+1][j+1][0], 1 if is_visible else data[i+1][j+1][1])

    for row in data:
        s=""
        for tree in row:
            if tree[1]:
                s+="#"
            else:
                s+=" "
        print(s)

    counts = [sum([a[1] for a in x]) for x in data]
    return sum(counts)

def solve_p2(data):
    data   = [[(int(y),None) for y in x] for x in data]
    scores = []
    for i, _ in enumerate(data): #issues iwth X5535
        for j, _ in enumerate(data):
            viewdirs = get_fullrows(data,i,j)
            score=1
            for _ in range(viewdirs.count([])):
                viewdirs.remove([])
                score*=0
            #print(viewdirs)
            for each in viewdirs:
                numvis=0
                for tree in each:
                    numvis+=1
                    if tree >= data[i][j][0]:
                        break
                score*=numvis
            scores.append(score)
    #for i in range(5):
        #print(scores[5*i:5*(i+1)])
    return max(scores)
