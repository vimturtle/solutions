from collections import Counter


with open("input/day6.txt") as f:
    fish = [int(n) for n in f.read().strip().split(",")]


def simulation(fish, days):
    counter = Counter(fish)
    for _ in range(days):
        counter = Counter({k - 1: counter[k] for k in counter})
        if -1 in counter.keys():
            counter[6] += counter[-1]
            counter[8] = counter[-1]
            del counter[-1]

    return sum(counter.values())


print(simulation(fish, 80), simulation(fish, 256))
