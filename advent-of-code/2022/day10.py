with open("input/day10.txt") as f:
    input = f.read().splitlines()


X, cycle, signal, crt = 1, 1, {}, [[" "] * 40 for _ in range(6)]


def check():
    if cycle % 40 == 20:
        signal[cycle] = X * cycle

    k = cycle - 1
    if abs((k % 40) - X) <= 1:
        crt[k // 40][k % 40] = "#"


for line in input:
    op, *args = line.split()
    cycle += 1
    check()

    if op == "addx":
        X += int(args[0])
        cycle += 1
        check()


print(sum(signal.values()))
print("\n".join("".join(ln) for ln in crt))
