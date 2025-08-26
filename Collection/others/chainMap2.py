from collections import ChainMap

d1 = {"x": 1, "y": 2}
d2 = {"y": 3, "z": 4}
cm = ChainMap(d1, d2)

print(cm["y"])  # Takes from d1
print(cm["z"])  # From d2
