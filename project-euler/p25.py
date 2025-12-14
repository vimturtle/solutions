a, b, i = 1, 1, 2

while True:
    a, b = b, a+b
    if len(str(b)) > 999:
        print(i+1)
        break
    i += 1
