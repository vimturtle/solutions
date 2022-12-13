import math


def is_prime(x):
    """
    Test if x is prime
    """
    if x <= 1:
        return False

    if x <= 3:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False

    return True


def primes(limit):
    """
    Generate primes upto limit using the Sieve of Eratosthenes
    """
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


def nth_prime(n):
    """
    Returns the nth prime number starting (n_1 = 2)
    """
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]
