from itertools import groupby
from pipe import where

def process(string):
    return eval(string)

def compare(pairL, pairR):
    match pairL, pairR:
        case int(), int():
            return (pairL > pairR) - (pairL < pairR) 
        case int(), list():
            return compare(pairL, [pairR])
        case list(), int():
            return compare([pairL], pairR)
        case list(), list():
            mapped = map(lambda a,b: (a > b) - (a < b), pairL, pairR)
            for each in mapped:
                if each in [-1,1]: return each
            return (lambda a,b: (a > b) - (a < b))(pairL, pairR)

    
def solve_p1(data):
    data = [list(group) for k, group in groupby(data, lambda x: x == "") if not k]
    pairs = []
    for pairL, pairR in data:
        pairL, pairR = process(pairL), process(pairR)
        pairs.append([pairL, pairR])

    indexes_running_total=0
    for index,(pairL, pairR) in enumerate(pairs):
        print(pairL, pairR)
        x = compare(pairL, pairR)
        print(x)
        if x:
            indexes_running_total+=index+1

    return indexes_running_total


def solve_p2(data):
    return "havent done p2"