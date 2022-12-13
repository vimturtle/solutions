import re
from collections import Counter


with open("input/day5.txt") as f:
    lines = [
        [int(n) for n in re.findall(r"\d+", line)] for line in f.read().splitlines()
    ]


def get_range(*args):
    return range(min(args), max(args) + 1)


def get_points(line):
    x1, y1, x2, y2 = line

    if x1 == x2:
        return [(x1, y) for y in get_range(y1, y2)]
    if y1 == y2:
        return [(x, y1) for x in get_range(x1, x2)]

    return []


def part1(lines):
    counts = Counter(sum(map(get_points, lines), []))
    return sum(counts[point] >= 2 for point in counts)


print(part1(lines))
