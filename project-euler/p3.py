import math

n = 600851475143
maxf = 1

while n % 2 == 0:
    n //= 2

for f in range(3, math.isqrt(n)+1, 2):
    while n % f == 0:
        n //= f
        maxf = f

if n > 1:
    maxf = n

print(maxf)
