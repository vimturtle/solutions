a, b, i = 1, 1, 2

while True:
    a, b = b, a+b
    i += 1
    if len(str(b)) > 999:
        print(i)
        break
