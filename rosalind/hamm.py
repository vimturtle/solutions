with open("input/hamm.txt") as f:
    s1, s2 = f.read().splitlines()
    print(sum([a != b for a, b in zip(s1, s2)]))
