with open("input/day9.txt") as f:
    motions = f.read().strip().splitlines()


knots = [(0, 0)] * 10
tails1, tails9 = set(), set()

direcs = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def add(t1, t2):
    return tuple(sum(x) for x in zip(t1, t2))


def diff(t1, t2):
    return tuple([abs(t1[i] - t2[i]) for i in range(len(t1))])


def move(head, tail, direc):
    _head = add(head, direcs[direc])
    _tail = tail

    d = diff(_head, tail)
    if d in [(2, 0), (0, 2)]:
        _tail = add(tail, direcs[direc])
    elif d in [(2, 1), (1, 2)]:
        _tail = head

    return _head, _tail


def move10(knots, direc):
    _head = add(knots[0], direcs[direc])
    new = [_head]

    for knot in knots[1:]:
        _tail = knot
        d = diff(_head, _tail)
        if d in [(2, 0), (0, 2)]:
            _tail = add(knot, direcs[direc])
        elif d in [(2, 1), (1, 2)]:
            _tail = _head

        new.append(_tail)
        _head = _tail

    return new


for motion in motions:
    direc, steps = motion.split()

    for i in range(int(steps)):
        knots = move10(knots, direc)
        tails1.add(knots[1])
        tails9.add(knots[9])


print(tails1, "\n\n", tails9)
print(len(tails1), len(tails9))
