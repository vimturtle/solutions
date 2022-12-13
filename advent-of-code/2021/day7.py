with open("input/day7.txt") as f:
    positions = [int(n) for n in f.read().strip().split(",")]


def cost(src, dest, expensive):
    dist = abs(src - dest)
    return dist if not expensive else dist * (dist + 1) // 2


print(
    min(sum(cost(p, pos, False) for p in positions) for pos in set(positions)),
    min(sum(cost(p, pos, True) for p in positions) for pos in set(positions)),
)
