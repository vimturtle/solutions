with open("input/day9.txt", "r") as f:
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]


def extrapolate(line):
    diffs = [b - a for a, b in zip(line, line[1:])]
    return line[-1] + extrapolate(diffs) if line else 0


print(sum(extrapolate(line) for line in lines))
print(sum(extrapolate(line[::-1]) for line in lines))
