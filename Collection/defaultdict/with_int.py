from collections import defaultdict

dd = defaultdict(int)
words = ["a", "b", "a", "c", "b", "a"]

for w in words:
    dd[w] += 1

print(dd)
