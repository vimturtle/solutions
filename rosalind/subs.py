with open("input/subs.txt") as f:
    s, t = f.read().splitlines()

    print(" ".join([str(i + 1) for i in range(len(s)) if s.startswith(t, i)]))
