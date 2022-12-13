import re


with open("input/day5.txt") as f:
    stacklines, commands = [part.split("\n") for part in f.read().strip().split("\n\n")]


stacks = []
i = 1
while True:
    try:
        stacks.append("".join([ln[i] for ln in stacklines[:-1] if ln[i] != " "]))
        i += 4
    except IndexError:
        break


def move(command, stacks, at_once):
    n, src, dest = [int(num) for num in re.findall(r"\d+", command)]
    _stacks = stacks.copy()
    takeout = stacks[src - 1][:n]
    _stacks[src - 1] = stacks[src - 1][n:]
    _stacks[dest - 1] = (takeout if at_once else takeout[::-1]) + stacks[dest - 1]

    return _stacks


new1 = new2 = stacks
for command in commands:
    new1 = move(command, new1, at_once=False)
    new2 = move(command, new2, at_once=True)


print(" ".join(["".join([stack[0] for stack in s]) for s in (new1, new2)]))
