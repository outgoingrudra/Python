from collections import Counter

stock = Counter(apples=10, bananas=5, oranges=7)
sold = Counter(apples=3, bananas=2)

remaining = stock - sold
print("Remaining Stock:", remaining)
