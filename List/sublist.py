nums = [1, 2, 3]
sublists = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
        sublists.append(nums[i:j])
print(sublists)
