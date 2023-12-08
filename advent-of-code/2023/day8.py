import math


with open("input/day8.txt", "r") as f:
    info = f.read().splitlines()
    direcs = info[0]
    coords = {coord[:3]: (coord[7:10], coord[12:15]) for coord in info[2:]}


def follow(start, is_ghost=False):
    steps = 0
    head = start

    while (not head.endswith("Z")) if is_ghost else (head != "ZZZ"):
        head = coords[head][0 if direcs[steps % len(direcs)] == "L" else 1]
        steps += 1

    return steps


p1 = follow("AAA")
p2 = math.lcm(
    *[follow(head, is_ghost=True) for head in coords.keys() if head.endswith("A")]
)

# LCM for part 2 doesn't generalize for all inputs.
# A general approach would be to use the Chinese remainder theorem.

print(p1, p2)
