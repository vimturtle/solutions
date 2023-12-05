with open("input/day4.txt", "r") as f:
    cards = f.read().splitlines()

p1 = 0
p2 = {k + 1: 1 for k in range(len(cards))}

for cardid, card in enumerate(cards, 1):
    nums = card.split(": ")[1].split(" | ")
    num_common = len([x for x in nums[0].split() if x in nums[1].split()])

    if num_common:
        p1 += 2 ** (num_common - 1)

        for i in range(p2[cardid]):
            for j in range(num_common):
                p2[cardid + j + 1] += 1

print(p1, sum(p2.values()))
