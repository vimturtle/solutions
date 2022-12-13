with open("input/day4.txt") as f:
    pairs = f.read().splitlines()


pairsets = [
    (set(range(x1, x2 + 1)), set(range(y1, y2 + 1)))
    for ((x1, x2), (y1, y2)) in [
        tuple(tuple(map(int, elfs.split("-"))) for elfs in pair.split(","))
        for pair in pairs
    ]
]


print(
    sum(x.issubset(y) or y.issubset(x) for x, y in pairsets),
    sum(len(x.intersection(y)) > 0 for x, y in pairsets),
)
