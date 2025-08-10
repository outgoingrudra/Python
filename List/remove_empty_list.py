lists = [1, [], 2, [], 3, [4, 5], []]
lists = [i for i in lists if i != []]
print("After removal:", lists)
