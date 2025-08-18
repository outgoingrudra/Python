import random

while True:
    print("You rolled:", random.randint(1, 6))
    ch = input("Roll again? (y/n): ")
    if ch.lower() != "y":
        break
