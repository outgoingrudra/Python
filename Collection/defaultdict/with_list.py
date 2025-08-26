from collections import defaultdict

dd = defaultdict(list)
pairs = [("fruit", "apple"), ("fruit", "banana"), ("color", "red")]

for k, v in pairs:
    dd[k].append(v)

print(dd)
