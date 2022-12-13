with open("input/day2.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]


h = d = aim = 0

for input in inputs:
    command = input.split()[0]
    value = int(input.split()[1])
    if command == "forward":
        h += value
        d += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(h * aim, h * d)
