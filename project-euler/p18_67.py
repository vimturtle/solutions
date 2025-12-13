p_id = 18
# p_id = 67 # Same problem but bigger triangle

with open(f'input/p{p_id}.txt') as f:
    lines = [[int(_) for _ in line.split()] for line in f.readlines()]


for r in range(len(lines) - 2, -1, -1):
    for c in range(len(lines[r])):
        lines[r][c] += max(lines[r+1][c], lines[r+1][c+1])


print(lines[0][0])
