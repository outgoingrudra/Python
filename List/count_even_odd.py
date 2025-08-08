nums = [10, 21, 4, 45, 66, 93]
even = 0
odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "| Odd:", odd)
