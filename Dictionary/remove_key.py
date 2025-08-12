data = {"a": 1, "b": 2, "c": 1, "d": 3}
value_to_remove = 1
filtered = {k: v for k, v in data.items() if v != value_to_remove}
print(filtered)
