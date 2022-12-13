###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """

    tab = [None] * (target_weight + 1)
    tab[0] = 0

    for i in range(target_weight):
        if tab[i] != None:
            for w in egg_weights:
                min_eggs = tab[i] + 1
                try:
                    if tab[i + w] is None or tab[i + w] > min_eggs:
                        tab[i + w] = min_eggs
                except IndexError:
                    continue

    return tab[target_weight]


# An alternative solution with a slightly different specification.
def dp_make_weight_alt(egg_weights, target_weight, memo={}):
    """
    Find the combination of egg weights to bring back. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: list, the best combination of eggs needed to make target weight
    """

    # Using tabulation
    tab = [None] * (target_weight + 1)
    tab[0] = []

    for i in range(target_weight):
        if tab[i] != None:
            for w in egg_weights:
                comb = tab[i] + [w]
                try:
                    if tab[i + w] is None or len(tab[i + w]) > len(comb):
                        tab[i + w] = comb
                except IndexError:
                    continue

    return sorted(tab[target_weight], reverse=True)

    # Using memoization
    # if target_weight in memo:
    #     return memo[target_weight]
    # if target_weight == 0:
    #     return []
    # if target_weight < 0:
    #     return None

    # min_comb = None

    # for w in egg_weights:
    #     new_comb = dp_make_weight_alt(egg_weights, target_weight - w, memo)
    #     if new_comb != None:
    #         comb = new_comb + [w]
    #         if min_comb == None or len(comb) < len(min_comb):
    #             min_comb = comb

    # memo[target_weight] = min_comb
    # return min_comb


def format_comb(comb):
    """
    >>> format_comb([25, 10, 25, 1, 10, 1, 10])
    2 * 25 + 3 * 10 + 2 * 1 = 82
    """

    counts = {}
    for i in sorted(comb, reverse=True):
        counts[i] = counts.get(i, 0) + 1

    t = ""
    for k, v in counts.items():
        if v != 0:
            t += f"{v} * {k} + "

    return f"{len(comb)} ({t[:-2]}= {sum(comb)})"


def dp_make_weight_greedy(egg_weights, target_weight):
    weights = list(egg_weights)
    target = target_weight
    result = 0
    comb = []
    while target > 0:
        m = target // max(weights)
        target -= m * max(weights)
        result += m
        comb += [max(weights)] * m
        weights.remove(max(weights))

    return result, comb


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == "__main__":
    egg_weights = (1, 5, 16, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    # print("Actual output:", format_comb(dp_make_weight_alt(egg_weights, n)))
    # print("Actual output:", dp_make_weight_greedy(egg_weights, n))
    print()
