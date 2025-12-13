from math import prod

with open('input/p11.txt') as f:
    grid = [[int(_) for _ in l.split()] for l in f.readlines()]

ROWS = len(grid)
COLS = len(grid[0])
N = 4
res = {"best_res": 0, "best_vals": [], "best_coords": []}
counts = {'h': 0, 'v': 0, 'd1': 0, 'd2': 0}

def update(loc, vals, coords):
    counts[loc] += 1
    p = prod(vals)
    if p > res["best_res"]:
        res["best_res"] = p
        res["best_vals"] = vals
        res["best_coords"] = coords

for r in range(ROWS):
    # Horizontal lines _
    for c in range(COLS-N+1):
        vals = grid[r][c:c+N]
        coords = [(r, c+_) for _ in range(N)]
        update('h', vals, coords)
    
    # Diagonals
    if r < ROWS-N+1:
        for c in range(COLS-N+1):
            # Main diagonal \
            vals = [grid[r+_][c+_] for _ in range(N)] 
            coords = [(r+_, c+_) for _ in range(N)]
            update('d1', vals, coords)
            
            # Anti diagonal /
            vals = [grid[r+N-1-_][c+_] for _ in range(N)]
            coords = [(r+N-1-_, c+_) for _ in range(N)]
            update('d2', vals, coords)

# Vertical lines |
for c in range(COLS):
    for r in range(ROWS-N+1):
        vals = [grid[r+_][c] for _ in range(N)]
        coords = [(r+_, c) for _ in range(N)]
        update('v', vals, coords)


print("Biggest product:", res["best_res"], str(res["best_vals"]))
print("found at", res["best_coords"])
print("among", sum(counts.values()), "products")
print("-", counts['h'], "in horizontal lines")
print("-", counts['v'], "in vertical lines")
print("-", counts['d1'], "in main diagonals")
print("-", counts['d2'], "in anti diagonals")

