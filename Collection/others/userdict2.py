from collections import UserDict

class NoDeleteDict(UserDict):
    def __delitem__(self, key):
        raise RuntimeError("Deletion not allowed")

d = NoDeleteDict({"x": 1})
print(d)
# del d["x"] -> will raise error
