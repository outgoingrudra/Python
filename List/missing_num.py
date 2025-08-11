nums = [1, 3, 5, 6]
start, end = 1, 6
missing = [i for i in range(start, end+1) if i not in nums]
print(missing)
