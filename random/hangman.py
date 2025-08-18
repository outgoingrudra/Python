import random

words = ["python", "hangman", "programming", "random"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    letter = input("Guess a letter: ").lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)
if "_" not in guessed:
    print("You guessed the word:", word)
else:
    print("You lost! The word was:", word)
