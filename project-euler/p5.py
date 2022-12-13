from math import gcd


# https://en.wikipedia.org/wiki/Least_common_multiple#Calculation
lcm = 1

for n in range(2, 21):
    lcm *= n // gcd(n, lcm)

print(lcm)
