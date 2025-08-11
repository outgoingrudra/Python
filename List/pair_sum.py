nums = [1, 2, 3, 4, 5, 6]
target = 7
pairs = set()
for i in nums:
    if (target - i) in nums:
        pairs.add(tuple(sorted((i, target - i))))
print(pairs)
