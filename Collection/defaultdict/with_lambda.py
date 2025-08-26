from collections import defaultdict

dd = defaultdict(lambda: "Not Found")
dd["name"] = "Rudra"
print(dd["name"])
print(dd["age"])
