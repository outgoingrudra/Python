from collections import Counter

nums = [1, 2, 2, 3, 4, 4, 4, 5]
count = Counter(nums)
print("Most Common Element:", count.most_common(1))
