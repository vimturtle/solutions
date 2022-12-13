with open("input/day6.txt") as f:
    input = f.read().rstrip()


def detect_marker(uniq):
    tmp = ""
    for i, c in enumerate(input):
        tmp = f"{tmp}{c}"[-uniq:]
        if len(set(tmp)) == uniq:
            return i + 1


print(detect_marker(4), detect_marker(14))
