from collections import defaultdict
from itertools import accumulate


with open("input/day7.txt") as f:
    input = f.read().strip().splitlines()[1:] # Skipping first line


sizes = defaultdict(int)
cwd = ['/']


# Thanks to u/4HbQ for this elegant technique
for line in input:
    match line.split():
        case '$', 'cd', '..': cwd.pop()
        case '$', 'cd', dirr: cwd.append(dirr + '/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for p in accumulate(cwd):
                sizes[p] += int(size)


print(sum(s for s in sizes.values() if s <= 100_000),
      min(s for s in sizes.values() if s >= sizes['/'] - 40000000))
