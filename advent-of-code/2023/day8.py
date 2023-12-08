import math

with open("input/day8.txt", "r") as f:
    info = f.read().splitlines()
    direcs = info[0]
    coords = info[2:]

    coord_dict = {}
    for coord in coords:
        k = coord[:3]
        v = (coord[7:10], coord[12:15])
        coord_dict[k] = v


def follow(start, is_ghost=False):
    steps = 0
    head = start

    while (not head.endswith("Z")) if is_ghost else (head != "ZZZ"):
        head = coord_dict[head][0 if direcs[steps % len(direcs)] == "L" else 1]
        steps += 1

    return steps


p1 = follow("AAA")
p2 = math.lcm(
    *[follow(head, is_ghost=True) for head in coord_dict.keys() if head.endswith("A")]
)

print(p1, p2)
