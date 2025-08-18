import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(nums)

print("Shuffled numbers:", nums)
guess = int(input("Guess the first number in shuffled list: "))

if guess == nums[0]:
    print("Correct guess!")
else:
    print("Wrong! The first number was", nums[0])
