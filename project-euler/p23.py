def divs(n):
    # Returns a set of all divisors of n
    divs = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        i += 1
    return divs

def sumdivs(n, proper=True):
    # Returns sum of divisors of n
    return sum(divs(n)) - (n if proper else 0)

limit = 28123 # 20161, See https://oeis.org/A048242
abun = [n for n in range(1, limit+1) if sumdivs(n) > n]
is_sum = [False] * (limit+1)

for i, m in enumerate(abun):
    for n in abun[i:]:
        s = m + n
        if s > limit:
            break
        is_sum[s] = True

print(sum(i for (i, c) in enumerate(is_sum) if not c))
