prices = {"apple": 50, "banana": 20, "mango": 80}
max_item = max(prices, key=prices.get)
print("Item with highest price:", max_item)
