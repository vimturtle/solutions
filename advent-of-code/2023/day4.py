with open("input/day4.txt", "r") as f:
    cards = f.read().splitlines()

p1 = 0
p2 = {k + 1: 1 for k in range(len(cards))}

for cardid, card in enumerate(cards, 1):
    win, have = map(str.split, card.split(": ")[1].split(" | "))
    num_common = len(set(win) & set(have))

    if num_common:
        p1 += 2 ** (num_common - 1)

        for i in range(num_common):
            p2[cardid + i + 1] += p2[cardid]

print(p1, sum(p2.values()))
