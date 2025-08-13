keys = ["apple", "banana", "mango", "orange"]
values = [60, 30, 80, 45]

result = {k: v for k, v in zip(keys, values) if v > 50}
print(result)
