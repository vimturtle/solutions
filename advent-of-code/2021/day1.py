with open("input/day1.txt", "r") as f:
    inputs = [int(line.rstrip()) for line in f.readlines()]


part_1 = sum(x < y for x, y in zip(inputs, inputs[1:]))

# For part 2, we just need to compare value 3 indices ahead!
# Since [a, b, c, d], `b + c + d`` is greater than `a + b + c` iff d > a
part_2 = sum(x < y for x, y in zip(inputs, inputs[3:]))
print(part_1, part_2)
