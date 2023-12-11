with open("input/bins.txt", "r") as f:
    _, _, s, elems = f.read().splitlines()
    s = [int(x) for x in s.split()]
    elems = [int(x) for x in elems.split()]

output = []


def bin_search(val, elems):
    """
    If val exists in elems list, returns index of val in elems
    Otherwise returns None
    """

    left, right = 0, len(elems) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_el = elems[mid]

        if mid_el == val:
            return mid
        if mid_el < val:
            left = mid + 1
        elif mid_el > val:
            right = mid - 1


for el in elems:
    found_idx = bin_search(el, s)
    output.append(str(-1 if found_idx is None else found_idx + 1))


print(" ".join(output))
