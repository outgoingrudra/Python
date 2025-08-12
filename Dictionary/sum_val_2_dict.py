dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
merged = dict1.copy()
for k, v in dict2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)
