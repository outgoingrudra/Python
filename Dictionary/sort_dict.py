data = {"apple": 50, "banana": 20, "mango": 80}
asc = dict(sorted(data.items(), key=lambda x: x[1]))
desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)
