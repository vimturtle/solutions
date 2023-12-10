with open("input/fibo.txt") as f:
    n = int(f.read())


fibs = {0: 0, 1: 1}


def fib(n):
    if n in fibs:
        return fibs[n]

    fibs[n] = fib(n - 1) + fib(n - 2)
    return fibs[n]


print(fib(n))
