from collections import Counter


with open("input/day3.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]


def part1(inputs):
    gamma = epsilon = ""

    for i in range(len(inputs[0])):
        common = Counter([x[i] for x in inputs])
        if common["1"] > common["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    power_consumption = int(gamma, 2) * int(epsilon, 2)
    return power_consumption


def part2(inputs):
    def get_rating(type):
        filtered = inputs.copy()

        for i in range(len(inputs[0])):
            common = Counter([x[i] for x in filtered])
            if len(filtered) == 1:
                break
            if common["1"] >= common["0"]:
                filtered = [x for x in filtered if x[i] == ("1" if type == "o2" else "0")]
            else:
                filtered = [x for x in filtered if x[i] == ("0" if type == "o2" else "1")]

        return int(filtered[0], 2)

    life_support_rating = get_rating("o2") * get_rating("co2")
    return life_support_rating


print(part1(inputs), part2(inputs))
