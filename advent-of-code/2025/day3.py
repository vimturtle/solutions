with open("input/day3.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]


def jolt(bnk, n, j=''):
    if n < 2:
        return j+max(bnk)
    mx = max(bnk[:-(n-1)])
    idx = bnk.index(mx)
    return jolt(bnk[idx+1:], n-1, j+mx)

def out_jolt(n):
    return sum(int(jolt(bnk, n)) for bnk in inputs)

print(out_jolt(2), out_jolt(12))
