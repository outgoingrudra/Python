from collections import Counter

list1 = [1, 2, 2, 3, 4, 4]
list2 = [2, 2, 3, 5, 4]

common = Counter(list1) & Counter(list2)
print("Common Elements with counts:", common)
