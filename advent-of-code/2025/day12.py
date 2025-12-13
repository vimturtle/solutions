# This is an exact cover problem
# The actual solution to these problems is very complicated
# This naive approach solves it for these inputs

import math


with open('input/day12.txt') as f:
    *presents, grids = f.read().split('\n\n')

SIZES = [sum(1 for _ in p if _ == '#') for p in presents]
p1 = 0
threshold = 1.25

for g in grids.splitlines():
    area, *nums = g.split()
    grid_area = math.prod(map(int, area[:-1].split('x')))
    present_area = sum([SIZES[i] * int(n) for i, n in enumerate(nums)])
    
    if grid_area > present_area*threshold:
        p1 += 1

print(p1)
