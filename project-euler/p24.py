import itertools as it


tmp = it.islice(it.permutations('0123456789'), 999999, None)
print("".join(next(tmp)))
