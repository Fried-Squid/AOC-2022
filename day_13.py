from itertools import groupby

def process(string):
    return eval(string)

def compare(pairL, pairR):
    if type(pairL) == int and type(pairR) == int:
        return pairL <= pairR
    elif type(pairL) == list and type(pairR) == int:
        return compare(pairL, [pairR])
    elif type(pairR) == list and type(pairL) == int:
        return compare([pairL], pairR)
    else: #both are lists:
        temp=[]
        if len(pairL) > len(pairR):
            return False
        for i in range(min([len(pairL), len(pairR)])):
            temp.append(compare(pairL[i], pairR[i]))
        return all(temp)

    
def solve_p1(data):
    data = [list(group) for k, group in groupby(data, lambda x: x == "") if not k]
    pairs = []
    for pairL, pairR in data:
        pairL, pairR = process(pairL), process(pairR)
        pairs.append([pairL, pairR])

    indexes_running_total=0
    for index,(pairL, pairR) in enumerate(pairs):
        if compare(pairL, pairR):
            indexes_running_total+=index
    
    return indexes_running_total


def solve_p2(data):
    pass