from functools import cache

with open('input/day11.txt') as f:
    inputs = [line.rstrip() for line in f.readlines()]
    
goal = 'out'
conns = {}
for line in inputs:
    src, dests = line.split(':')
    conns[src] = dests.split()

@cache
def p1(src):
    return 1 if src == goal else sum(p1(d) for d in conns[src])

@cache
def p2(src, dac=False, fft=False):
    if src == goal:
        return 1 if dac and fft else 0
    return sum(p2(d, dac or d=='dac', fft or d=='fft') for d in conns[src])

print(p1('you'), p2('svr'))
