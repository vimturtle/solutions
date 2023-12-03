import re

with open("input/day1.txt", "r") as f:
    lines = f.read().splitlines()


p1 = p2 = 0
word2num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

replacements = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

translate = lambda x: x if x.isdigit() else word2num[x]


for line in lines:
    n = [c for c in line if c.isdigit()]
    p1 += int(n[0] + n[-1])

    for k, v in replacements.items():
        line = line.replace(k, v)

    matches = re.findall(
        r"1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine", line
    )

    p2 += int(translate(matches[0]) + translate(matches[-1]))


print(p1, p2)
