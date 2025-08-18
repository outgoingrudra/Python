import random

words = ["python", "developer", "machine", "learning", "hackathon"]
secret = random.choice(words)
attempts = 5

print("Guess the secret word, it has", len(secret), "letters")

while attempts > 0:
    guess = input("Enter word: ")
    if guess == secret:
        print("You guessed it right!")
        break
    else:
        print("Wrong guess. Attempts left:", attempts-1)
    attempts -= 1
else:
    print("Out of attempts! The word was:", secret)
