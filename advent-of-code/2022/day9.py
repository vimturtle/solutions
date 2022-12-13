with open("input/day9.txt") as f:
    motions = f.read().strip().splitlines()


tails = set()
s = head = tail = (0, 0)
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


for motion in motions:
    direc, steps = motion.split()

    for i in range(int(steps)):
        head, tail = move(head, tail, direc)
        tails.add(tail)


print(len(tails))
