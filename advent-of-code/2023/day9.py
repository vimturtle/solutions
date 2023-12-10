with open("input/day9.txt", "r") as f:
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]


def extrapolate(l):
    diffs = [b - a for a, b in zip(l, l[1:])]
    return l[-1] + extrapolate(diffs) if l else 0


print(sum(extrapolate(line) for line in lines))
print(sum(extrapolate(line[::-1]) for line in lines))
