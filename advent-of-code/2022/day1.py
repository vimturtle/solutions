with open("input/day1.txt") as f:
    elfs = f.read().rstrip().split("\n\n")
    total_cals = [sum(int(x) for x in elf.split("\n")) for elf in elfs]


print(max(total_cals))
print(sum(sorted(total_cals, reverse=True)[:3]))
