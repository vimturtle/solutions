import re

with open("input/day2.txt", "r") as f:
    games = f.read().splitlines()

R, G, B = 12, 13, 14
p1 = p2 = 0

for game in games:
    gameid = int(re.findall(r"Game\s(\d+)", game)[0])
    r = [int(x) for x in re.findall(r"(\d+)\sred", game)]
    g = [int(x) for x in re.findall(r"(\d+)\sgreen", game)]
    b = [int(x) for x in re.findall(r"(\d+)\sblue", game)]

    if all(x <= R for x in r) and all(x <= G for x in g) and all(x <= B for x in b):
        p1 += gameid

    p2 += max(r) * max(g) * max(b)


print(p1, p2)
