import random

ticket = set()
while len(ticket) < 6:
    ticket.add(random.randint(1, 49))
print("Your lottery ticket numbers:", ticket)
