from math import prod


with open("input/p8.txt") as f:
    number = "".join(line for line in f.read().splitlines())


max_prod = 1

for i, n in enumerate(number):
    prod13 = prod(int(c) for c in number[i : i + 13])
    if prod13 > max_prod:
        max_prod = prod13


print(max_prod)
