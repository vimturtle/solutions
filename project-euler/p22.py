import string


with open("input/p22.txt") as f:
    names = sorted(f.read().rstrip()[1:-1].split('","'))


def score(name, pos):
    return sum(string.ascii_uppercase.index(c) + 1 for c in name) * pos


print(sum(score(name, i + 1) for i, name in enumerate(names)))
