from collections import OrderedDict

od = OrderedDict()
od["a"] = 100
od["c"] = 300
od["b"] = 200

for k, v in od.items():
    print(k, v)
