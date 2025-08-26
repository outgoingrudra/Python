from collections import namedtuple

Person = namedtuple("Person", "name age gender", rename=True)
p = Person("Rudra", 20, "M")
print(p)
