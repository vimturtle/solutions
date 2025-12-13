import math
from collections import defaultdict

# If n = a^p * b^q * c^r where a, b, c are prime factors
# of n, then number of all divisors of n equals
# (p+1)*(q+1)*(r+1)

def num_div(t):
    # Creates dict with prime factors of t as keys
    # and their powers as values
    # Returns num of divisors using the formula above
    n = t
    d = defaultdict(int)

    while n % 2 == 0:
        d[2] += 1
        n //= 2

    for f in range(3, math.isqrt(n)+1, 2):
        while n % f == 0:
            d[f] += 1
            n //= f

    if n > 1:
        d[n] += 1

    return math.prod([v+1 for v in d.values()])

# ith triangular number is given by t_i = i*(i+1) / 2
# An efficient approach for larger numbers is
# to count the num of divisors for i and (i+1)
# separately and multiply the result since they 
# are coprime. We should divide one of them by 2
# depending on which one is even

goal = 500
i = 0
while True:
    i += 1
    (a, b) = (i//2, i+1) if i % 2 == 0 else (i, (i+1) // 2)

    n_div = num_div(a) * num_div(b)

    if n_div > goal:
        ti = i*(i+1) // 2
        print(f"T({i}) = {ti} ({n_div} divisors)")
        break

