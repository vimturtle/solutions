with open("input/day9.txt") as f:
    motions = f.read().strip().splitlines()

direcs = {"U": 1j, "R": 1, "D": -1j, "L": -1}
knots = [0 + 0j] * 10
visited = [set([knot]) for knot in knots]
sign = lambda n: 0 if n == 0 else (-1, 1)[n > 0]


def follow(h, t):
    """Return distance the tail must travel to follow head"""
    dist = 0
    if abs(h - t) <= abs(1 + 1j):  # Adjacent
        return dist

    if h.real == t.real:  # Same vertical plane
        dist = sign(h.imag - t.imag) * 1j
    elif h.imag == t.imag:  # Same horizonal plane
        dist = sign(h.real - t.real)
    else:  # Diagonally apart
        dist = sign(h.real - t.real) + sign(h.imag - t.imag) * 1j

    return dist


for motion in motions:
    direc, steps = motion.split()

    for i in range(int(steps)):
        knots[0] += direcs[direc]

        for i in range(1, 10):
            knots[i] += follow(knots[i - 1], knots[i])
            visited[i].add(knots[i])

print(len(visited[1]), len(visited[9]))
