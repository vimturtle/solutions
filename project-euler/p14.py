from functools import cache


@cache
def chain_length(n):
    return 1 if n == 1 else chain_length(n // 2 if n % 2 == 0 else 3 * n + 1) + 1


print(max(range(1, 1000000), key=chain_length))
