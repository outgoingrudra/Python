nums = [5, 3, 8, 1, 2]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sorted list:", nums)
