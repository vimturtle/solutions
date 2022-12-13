from itertools import permutations
from pprint import pprint


with open("input/day8.txt") as f:
    notes = f.read().splitlines()


# Part 1
count = 0
for entry in notes:
    output = entry.split(" | ")[1]
    # Correspond to 1, 4, 7, 8 resp.
    count += sum(1 for value in output.split() if len(value) in (2, 4, 3, 7))


print(count)


# Part 2
segments = "abcdefg"
perms = list(permutations(segments))

segment_map = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


for entry in notes:
    for perm in perms:
        p = "".join(perm)
