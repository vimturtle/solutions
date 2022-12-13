import re
from math import prod, lcm
from operator import add, mul
from copy import deepcopy


with open("input/day11.txt") as f:
    monkeys = f.read().strip().split("\n\n")


def parse(expr):
    lhs, op, rhs = expr.split()
    return lambda x: (add if op == "+" else mul)(
        int(lhs) if lhs.isdigit() else x, int(rhs) if rhs.isdigit() else x
    )


bags, tests, passes, fails, ops = [], [], [], [], []


for monkey in monkeys:
    lines = monkey.split("\n")
    bags.append([int(d) for d in re.findall(r"\d+", lines[1])])
    ops.append(parse(lines[2].split(" = ")[-1]))
    tests.append(int(lines[3].split("by ")[-1]))
    passes.append(int(lines[4].split("monkey ")[-1]))
    fails.append(int(lines[5].split("monkey ")[-1]))


N = lcm(*tests)


def monkey_business(bags, rounds, relief):
    _bags = deepcopy(bags)
    inspects = [0] * len(bags)
    for _ in range(rounds):
        for i, bag in enumerate(_bags):
            while len(bag) > 0:
                new = ops[i](bag.pop(0)) % N
                if relief:
                    new //= 3
                _bags[passes[i] if new % tests[i] == 0 else fails[i]].append(new)
                inspects[i] += 1

    return prod(sorted(inspects)[-2:])


print(monkey_business(bags, 20, relief=True))
print(monkey_business(bags, 10000, relief=False))
