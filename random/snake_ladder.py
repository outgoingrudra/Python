import random

pos = 1
snakes = {16: 6, 48: 26, 64: 60, 93: 73}
ladders = {3: 22, 20: 38, 45: 62, 71: 92}

while pos < 100:
    roll = random.randint(1, 6)
    pos += roll
    if pos in snakes:
        pos = snakes[pos]
    elif pos in ladders:
        pos = ladders[pos]
    if pos > 100:
        pos = 100
    print("Rolled:", roll, "Current Position:", pos)
print("You reached 100! Game Over")
