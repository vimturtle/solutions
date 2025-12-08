from collections import defaultdict

with open("input/day7.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

p1 = 0
beams = {inputs[0].index('S'): 1}

for line in [_ for _ in inputs[1:] if '^' in _]:
    nb = defaultdict(int)
    for i, b in beams.items():
        if line[i] == '^':
            nb[i-1] += b
            nb[i+1] += b
            p1+=1
        else:
            nb[i] += b
    beams = nb

print(p1, sum(beams.values()))
