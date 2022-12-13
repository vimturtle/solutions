with open("input/p13.txt") as f:
    print(str(sum(int(num) for num in f.read().splitlines()))[:10])
