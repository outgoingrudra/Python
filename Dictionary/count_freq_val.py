data = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}
value_freq = {}
for val in data.values():
    value_freq[val] = value_freq.get(val, 0) + 1
print(value_freq)
