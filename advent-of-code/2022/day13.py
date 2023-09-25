with open("input/day13.txt") as f:
    packets = [[*map(eval, group.split())] for group in f.read().split("\n\n")]

p1 = 0
lt2 = 0  # Number of packets smaller than [[2]]
lt6 = 0  # Number of packets smaller than [[6]]


# Nice elegant trick from u/4HbQ
def cmp(l, r):
    match l, r:
        case int(), int():
            return l - r
        case int(), list():
            return cmp([l], r)
        case list(), int():
            return cmp(l, [r])
        case list(), list():
            for z in map(cmp, l, r):
                if z:
                    return z
            return cmp(len(l), len(r))


for i, pair in enumerate(packets, 1):
    if cmp(*pair) < 0:
        p1 += i
    for packet in [*pair]:
        if cmp(packet, [[2]]) < 0:
            lt2 += 1
        if cmp(packet, [[6]]) < 0:
            lt6 += 1

print(p1)

# Indices of [[2]] and [[6]] are 1 + num_packets smaller than them respectively.
# [[2]] is itself smaller than [[6]] so adding one more to lt6
print((lt2 + 1) * (lt6 + 1 + 1))
