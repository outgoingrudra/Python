from collections import ChainMap

d1 = {"a": 10}
d2 = {"b": 20}
cm = ChainMap(d1, d2)

cm["a"] = 100
print(d1)
