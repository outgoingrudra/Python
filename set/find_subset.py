from itertools import chain, combinations
s = {1, 2, 3}
subs = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
print(subs)
