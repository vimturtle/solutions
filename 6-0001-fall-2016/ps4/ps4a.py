# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def combine(letter, rest):
    """
    Returns a list of possible unique combinations
    of letter with each string in the list

    >>> combine('a', ['bc', 'cb'])
    ['cab', 'acb', 'bac', 'abc', 'cba', 'bca']
    """

    new = []
    for item in rest:
        new += [item[:i] + letter + item[i:] for i in range(len(item) + 1)]
    return list(set(new))


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    if len(sequence) == 1:
        return [sequence]
    else:
        return combine(sequence[0], get_permutations(sequence[1:]))


if __name__ == "__main__":
    #    #EXAMPLE
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", sorted(get_permutations(example_input)))
    print("---")

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    example_input = "zzz"
    print("Input:", example_input)
    print("Expected Output:", ["zzz"])
    print("Actual Output:", get_permutations(example_input))
    print("---")

    example_input = "aza"
    print("Input:", example_input)
    print("Expected Output:", ["aaz", "aza", "zaa"])
    print("Actual Output:", sorted(get_permutations(example_input)))
    print("---")

    example_input = "fact"
    print("Input:", example_input)
    print(
        "Expected Output:",
        sorted(
            [
                "fact",
                "afct",
                "cfat",
                "fcat",
                "acft",
                "caft",
                "tafc",
                "atfc",
                "ftac",
                "tfac",
                "aftc",
                "fatc",
                "fcta",
                "cfta",
                "tfca",
                "ftca",
                "ctfa",
                "tcfa",
                "tcaf",
                "ctaf",
                "atcf",
                "tacf",
                "catf",
                "actf",
            ]
        ),
    )
    print("Actual Output:", sorted(get_permutations(example_input)))
    print()
