from pipe import select, where, traverse
from functools import partial

class Monkey_p1:
    def __init__(self, id, items, operation, test, test_outcomes):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.test_outcomes = list(test_outcomes | select(int))
        self.inspections = 0

    def full_eval(self):
        res = []
        for _ in range(len(self.items)):
            res.append(self.eval())
        return res
    def eval(self):
        if len(self.items) >= 1:
            target = self.items.pop(0)
            opped = self.operation(target)//3
            outcome = self.test_outcomes[self.test(opped)]
            self.inspections+=1
            return opped, outcome
        else:
            return None, None

    def give(self, thing):
        self.items.append(thing)
def solve_p1(data):
    cur_id = 0
    test_outcomes = [0,0]
    monkeys=[]

    for line in data:
        if f"Monkey {cur_id+1}" in line:
            monkeys.append(Monkey_p1(cur_id,items,operation,test,test_outcomes))
            cur_id+=1
        elif line == "" or f"Monkey {cur_id}" in line:
            pass
        else:
            selector, datapoint = line.split(": ")
            if selector == "  Starting items":
                items = list(datapoint.split(", ") | select(lambda a:int(a)))
            elif selector == "  Operation":
                datapoint = datapoint.replace("new = ", "")
                if "+" in datapoint:
                    op = lambda a,b: a+b
                    datapoint = list(datapoint.split(" + ") | where(lambda a: a!="old"))
                elif "*" in datapoint:
                    op = lambda a, b: a * b
                    datapoint = list(datapoint.split(" * ") | where(lambda a: a!="old"))
                baseop1 = lambda f, a: f(a, a)
                baseop2 = lambda f, a, b: f(a, b)
                if len(datapoint) == 0:
                    operation = staticmethod(partial(baseop1, op))
                elif len(datapoint) == 1:
                    operation = staticmethod(partial(baseop2, op, int(datapoint[0])))
                else: print(datapoint)
            elif selector == "  Test":
                datapoint = int(datapoint.split("by ")[-1])
                test = staticmethod(partial(lambda b,a: a//b==a/b, datapoint))
            elif selector == "    If true":
                test_outcomes[True] = datapoint.split("monkey ")[-1]
            elif selector == "    If false":
                test_outcomes[False] = datapoint.split("monkey ")[-1]
    monkeys.append(Monkey_p1(cur_id,items,operation,test,test_outcomes))
    for i in range(20):
        for monkey in monkeys:
            moves = monkey.full_eval()
            for obj, to_pass in moves:
                if obj is not None:
                    print(obj, to_pass)
                    monkeys[to_pass].give(obj)

    print(list(monkeys | select(lambda a: a.inspections)))
    return sorted(list(monkeys | select(lambda a: a.inspections)))[::-1][0] * sorted(list(monkeys | select(lambda a: a.inspections)))[::-1][1]

class Monkey_p2:
    def __init__(self, id, items, operation, test, test_outcomes):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.test_outcomes = list(test_outcomes | select(int))
        self.inspections = 0
        if self.operation(1) - self.operation(2) == 1:
            self.linear = True
        else: self.linear = False

    def full_eval(self):
        res = []
        for _ in range(len(self.items)):
            res.append(self.eval())
        return res
    def eval(self):
        target = self.items.pop(0) # mod 9699690
        output = self.operation(target)
        target = output % 9699690
        self.inspections+=1
        return target, self.test_outcomes[target // self.test == target / self.test]
    def give(self, thing):
        self.items.append(thing)

def solve_p2(data):
    print("start 2")
    cur_id = 0
    test_outcomes = [0,0]
    monkeys=[]

    for line in data:
        if f"Monkey {cur_id+1}" in line:
            monkeys.append(Monkey_p2(cur_id,items,operation,test,test_outcomes))
            cur_id+=1
        elif line == "" or f"Monkey {cur_id}" in line:
            pass
        else:
            selector, datapoint = line.split(": ")
            if selector == "  Starting items":
                items = list(datapoint.split(", ") | select(lambda a:int(a)))
            elif selector == "  Operation":
                datapoint = datapoint.replace("new = ", "")
                if "+" in datapoint:
                    op = lambda a,b: a+b
                    datapoint = list(datapoint.split(" + ") | where(lambda a: a!="old"))
                elif "*" in datapoint:
                    op = lambda a, b: a * b
                    datapoint = list(datapoint.split(" * ") | where(lambda a: a!="old"))
                baseop1 = lambda f, a: f(a, a)
                baseop2 = lambda f, a, b: f(a, b)
                if len(datapoint) == 0:
                    operation = staticmethod(partial(baseop1, op))
                elif len(datapoint) == 1:
                    operation = staticmethod(partial(baseop2, op, int(datapoint[0])))
                else: print(datapoint)
            elif selector == "  Test":
                datapoint = int(datapoint.split("by ")[-1])
                test = datapoint
            elif selector == "    If true":
                test_outcomes[True] = datapoint.split("monkey ")[-1]
            elif selector == "    If false":
                test_outcomes[False] = datapoint.split("monkey ")[-1]
    monkeys.append(Monkey_p2(cur_id,items,operation,test,test_outcomes))
    for i in range(10000):
        for monkey in monkeys:
            moves = monkey.full_eval()
            for obj, to_pass in moves:
                if obj is not None:
                    monkeys[to_pass].give(obj)

    print(list(monkeys | select(lambda a: a.inspections)))
    return sorted(list(monkeys | select(lambda a: a.inspections)))[::-1][0] * sorted(list(monkeys | select(lambda a: a.inspections)))[::-1][1]