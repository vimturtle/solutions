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

def d(n, proper=True):
    # Returns sum of divisors of n
    return sum(divs(n)) - (n if proper else 0)

limit = 10000
total = 0

for n in range(2, limit):
    da = d(n)
    if da != n:
        db = d(da)
        if db == n:
            total += n

print(total)
