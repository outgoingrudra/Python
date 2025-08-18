import random
items = ["A", "B", "C"]
weights = [0.7, 0.2, 0.1]
print(random.choices(items, weights=weights, k=5))
