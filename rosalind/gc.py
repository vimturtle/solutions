with open("input/gc.txt") as f:
    lines = f.read().splitlines()

strings = {}
curr_id = None

for line in lines:
    if line.startswith(">"):
        curr_id = line[1:]
        strings[curr_id] = ""
    else:
        strings[curr_id] += line

max_gc_id, max_gc = "", 0

for k, v in strings.items():
    gc = len([c for c in v if c in ["C", "G"]]) * 100 / len(v)
    if gc > max_gc:
        max_gc_id = k
        max_gc = gc

print(max_gc_id + "\n" + str(round(max_gc, 6)))
