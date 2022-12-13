with open("input/day8.txt") as f:
    grid = f.read().strip().split("\n")


rows, cols = len(grid), len(grid[0])
visible_trees = maxscore = 0


for i in range(rows):
    for j in range(cols):
        if i in (0, rows - 1) or j in (0, cols - 1):
            visible_trees += 1
            continue

        visible, score = False, 1

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            _x, _y = i, j
            dist = 0

            while True:
                _x, _y = _x + dx, _y + dy
                in_grid = 0 <= _x < rows and 0 <= _y < cols
                if in_grid and grid[_x][_y] < grid[i][j]:
                    dist += 1
                    continue

                visible = visible or not in_grid
                score *= dist + in_grid
                break

        visible_trees += visible
        maxscore = max(maxscore, score)


print(visible_trees, maxscore)
