from collections import Counter

c1 = Counter(a=4, b=2)
c2 = Counter(a=1, b=3, c=5)

merged = c1 + c2
print("Merged Counter:", merged)
