from collections import Counter

items = ['a', 'b', 'a', 'c', 'b', 'a']
c = Counter(items)

expanded_list = list(c.elements())
print("Expanded List:", expanded_list)
