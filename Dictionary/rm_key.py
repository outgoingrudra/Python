data = {"a": 5, "b": 2, "c": 8, "d": 1}
threshold = 4
filtered = {k: v for k, v in data.items() if v >= threshold}
print(filtered)
