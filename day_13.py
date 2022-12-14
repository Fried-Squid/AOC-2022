from itertools import groupby
from pipe import where, select

def process(string):
    return eval(string)

def int_compare(x,y):
    return -1 if x>y else 0 if x==y else 1

def compare(pairL, pairR):
    typeL, typeR = isinstance(pairL, int), isinstance(pairR, int)
    if typeL and typeR:
        return int_compare(pairL, pairR)
    elif typeL and not typeR:
        return compare([pairL], pairR)
    elif not typeL and typeR:
        return compare(pairL, [pairR])
    elif not typeL and not typeR:
        for each in list(map(compare, pairL, pairR)):
            if each in [-1, 1]: return each
        return int_compare(len(pairL), len(pairR))

    
def solve_p1(data):
    data = [list(group) for k, group in groupby(data, lambda x: x == "") if not k]
    pairs = []
    for pairL, pairR in data:
        pairL, pairR = process(pairL), process(pairR)
        pairs.append([pairL, pairR])

    indexes_running_total=0
    for index,(pairL, pairR) in enumerate(pairs):
        mapped = list(map(compare, pairL, pairR))
        x = int_compare(len(pairL), len(pairR)) + 1
        for each in mapped:
            if each == -1:
                x = False
                break
            elif each == 1:
                x = True
                break
        print(mapped, x)
        if x:
            print(index+1)
            indexes_running_total+=index+1

    return indexes_running_total

def merge(left, right, greater_than):
    res = []
    while len(left) > 0 and len(right) > 0:
        if greater_than(left[0], right[0]):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while len(left)>0:
        res.append(left.pop(0))
    while len(right)>0:
        res.append(right.pop(0))

    return res

def merge_sort(a, greater_than):
    if len(a) <= 1:
        return a

    left,right = [],[]
    
    for i,x in enumerate(a):
        if i<len(a)/2:
            left.append(x)
        else:
            right.append(x)
    
    left = merge_sort(left, greater_than)
    right = merge_sort(right, greater_than)

    return merge(left, right, greater_than)

def solve_p2(data):
    data=list(data | where(lambda a:a!=""))
    data=list(data | select(process))
    data+=[[[6]], [[2]]]


    greater_than = lambda a,b: True if compare(a,b) == 1 else False
    data = merge_sort(data, greater_than)
    #print(data)
    return (data.index([[2]])+1) * (data.index([[6]])+1)
