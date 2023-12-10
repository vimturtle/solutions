with open("input/gc.txt") as f:
    lines = f.read().splitlines()

strings = {}
curr_id = None

for line in lines:
    if line.startswith(">"):
        strings[line] = ""
        curr_id = line
    else:
        strings[curr_id] += line

high_gc = 0
high_id = ""

for k, v in strings.items():
    gc = len([c for c in v if c in ["C", "G"]]) * 100 / len(v)
    if gc > high_gc:
        high_gc = gc
        high_id = k

print(high_id[1:] + "\n" + str(round(high_gc, 6)))
