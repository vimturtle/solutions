from matplotlib import pyplot as plt

with open("input/day13.txt") as f:
    marks, folds = [part.split("\n") for part in f.read().strip().split("\n\n")]
    marks = [tuple(int(n) for n in mark.split(",")) for mark in marks]


def fold(marks, command):
    axis, line = command.split()[2].split("=")

    if axis == "x":
        return {(int(line) - abs(int(line) - x), y) for (x, y) in marks}
    else:
        return {(x, int(line) - abs(int(line) - y)) for (x, y) in marks}


# Part 1
print(len(fold(marks, folds[0])))

# Part 2
newmarks = marks
for command in folds:
    newmarks = fold(newmarks, command)

plt.scatter(*zip(*newmarks), marker="o")
plt.axis("equal")
plt.axis("off")
plt.gca().invert_yaxis()
plt.show()
