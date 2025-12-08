with open("input/day5.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

empty = inputs.index("")
ids = [int(_) for _ in inputs[empty + 1 :]]
rngs = sorted(
    [
        range(int(r[0]), int(r[1]) + 1)
        for r in [rng.split("-") for rng in inputs[:empty]]
    ],
    key=lambda r: r[0],
)

p1 = 0

for i in ids:
    if any(i in rng for rng in rngs):
        p1 += 1

nrngs = [rngs[0]]
for rng in rngs[1:]:
    if rng.start > nrngs[-1].stop:
        nrngs.append(rng)
    else:
        nrng = range(nrngs[-1].start, max(nrngs[-1].stop, rng.stop))
        nrngs.pop()
        nrngs.append(nrng)

print(p1, sum(len(rng) for rng in nrngs))
