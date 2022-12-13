sum = 1000


for a in range(1, sum + 1):
    for b in range(a + 1, sum + 1):
        c = sum - a - b
        if a * a + b * b == c * c:
            print(a * b * c)
