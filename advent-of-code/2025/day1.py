with open("input/day1.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

pos, p1, p2 = 50, 0, 0

for m in inputs:
    d, n = m[0], int(m[1:])
    r, s = divmod(n, 100)
    p2 += r

    if d == 'R':
        npos = pos+s
        if npos > 99:
            npos -= 100
            if not npos == 0:
              p2 += 1
    elif d == 'L':
        npos = pos-s
        if npos < 0:
            npos += 100
            if not pos == 0:
              p2 += 1

    if npos == 0:
        p1 += 1
        p2 += 1

    pos = npos

print(p1, p2)
