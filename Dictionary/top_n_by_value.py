data = {"apple": 50, "banana": 20, "mango": 80, "orange": 60}
N = 2
top_items = sorted(data.items(), key=lambda x: x[1], reverse=True)[:N]
print("Top items:", dict(top_items))
