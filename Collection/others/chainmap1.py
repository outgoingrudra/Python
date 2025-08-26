from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
cm = ChainMap(dict1, dict2)
print(cm)
