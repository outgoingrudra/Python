import random

while True:
    guess = input("Guess heads or tails: ").lower()
    toss = random.choice(["heads", "tails"])
    print("Coin shows:", toss)
    if guess == toss:
        print("You guessed right!")
    else:
        print("Wrong guess!")
    if input("Play again? (y/n): ").lower() != "y":
        break
