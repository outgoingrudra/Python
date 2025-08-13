list_dicts = [{"a": 1, "b": 2}, {"a": 3, "c": 4}]
merged = {}
for d in list_dicts:
    for k, v in d.items():
        merged[k] = merged.get(k, 0) + v
print(merged)
