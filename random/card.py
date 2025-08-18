import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [r + " of " + s for s in suits for r in ranks]
random.shuffle(deck)

while deck:
    print("You drew:", deck.pop())
    if input("Draw again? (y/n): ").lower() != "y":
        break
