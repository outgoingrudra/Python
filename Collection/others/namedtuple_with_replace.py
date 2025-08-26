from collections import namedtuple

Car = namedtuple("Car", "brand price")
c1 = Car("Tesla", 60000)
c2 = c1._replace(price=65000)
print(c1)
print(c2)
