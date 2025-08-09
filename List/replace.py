nums = [1, 2, 3, 4, 5]
old = 3
new = 99
nums = [new if i == old else i for i in nums]
print("After replacement:", nums)
