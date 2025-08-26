from collections import UserDict

class MyDict(UserDict):
    def remove(self, key):
        if key in self.data:
            del self.data[key]

d = MyDict({"a": 1, "b": 2})
d.remove("a")
print(d)
