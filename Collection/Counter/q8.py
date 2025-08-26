from collections import Counter

data = [5, 5, 5, 2, 2, 3, 3, 3, 3, 4]
count = Counter(data)
k = 2
result = [item for item, freq in count.items() if freq > k]
print("Elements appearing more than", k, "times:", result)
