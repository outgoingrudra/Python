from collections import OrderedDict

od = OrderedDict([("x", 10), ("y", 20), ("z", 30)])
od.move_to_end("x")
print(od)

od.move_to_end("z", last=False)
print(od)
