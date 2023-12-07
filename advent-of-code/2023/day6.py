import math


with open("input/day6.txt", "r") as f:
    lines = f.read().splitlines()
    times, distances = [line.split(":")[1].lstrip().split() for line in lines]

p1 = 1


def get_num_wins(T, D):
    """
    t = T - B    ....(1)
    D = t * B    ....(2)

    where
    t = travel time
    T = total race time
    B = button press time
    D = distance travelled

    Substituting (1) in (2) and simplifying, we get
    B^2 - T*B + D = 0

    Now we can use the quadratic formula to solve for B
    """
    b1 = (T + math.sqrt(pow(T, 2) - 4 * D)) / 2
    b2 = (T - math.sqrt(pow(T, 2) - 4 * D)) / 2

    return math.ceil(b1) - math.floor(b2) - 1


for time, dist in zip(times, distances):
    p1 *= get_num_wins(int(time), int(dist))


p2 = get_num_wins(int("".join(times)), int("".join(distances)))


print(p1, p2)
