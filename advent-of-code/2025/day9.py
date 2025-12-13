from itertools import combinations

with open("input/day9.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

inputs = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split('\n')

area = lambda c: (abs(c[1][1] - c[0][1]) + 1)*(abs(c[1][0] - c[0][0]) + 1)

reds = [(tuple(map(int, reversed(c.split(','))))) for c in inputs]
combs = sorted(combinations(reds, 2), key=area, reverse=True)

print(area(combs[0]))


p1, p2 = 0, 0

sorter = lambda l:[((min(a,c),min(b,d)),(max(a,c), max(b,d))) for (a,b),(c,d) in l]

lines = sorted([c for c in combs if c[0][1] == c[1][1] or c[0][0]==c[1][0]], key=sorter)
print(lines, len(lines))

for (a, b), (c, d) in combs:
    area = (abs(d-b) + 1)*(abs(c-a) + 1)
    print(area)
    
    if area > p1:
        p1 = area

    if area > p2:
        for (p, q), (r, s) in lines:
            if not (p<c and q<d and r>a and s>b):
                p2 = area

print(p1, p2)
# 
# for r1, r2 in lines:
#     if r1[0] == r2[0]:
#         for p in range(1, abs(r2[1]-r1[1])):
#             greens.add((r1[0], r1[1] + p))
#     if r1[1] == r2[1]:
#         for p in range(1, abs(r2[0]-r1[0])):
#             greens.add((r1[0] + p, r1[1]))
# 
# boundary = sorted(reds + list(greens))
# 
# p2 = 0
# for r1, r2 in combs:
#      area = 
# 
# 
# print(boundary)
# 
