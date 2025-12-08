import math, itertools

with open("input/day6.txt", "r") as f:
    inputs = [line.replace('\n', '') for line in f.readlines()]


p1 = 0
p = [line.split() for line in inputs]
ops = p[-1]
ans = lambda i,l: sum(l) if ops[i] == '+' else math.prod(l)
for i, nums in enumerate(zip(*p[:-1])):
    p1 += ans(i, [int(_) for _ in nums])

p2 = 0
pp = [''.join(_).replace(' ', '') for _ in zip(*inputs[:-1])]
res = []
for k, g in itertools.groupby(pp, key=lambda x: x==''):
    if not k:
        res.append([int(_) for _ in g])
for i, l in enumerate(res):
    p2 += ans(i, l)

print(p1, p2)
