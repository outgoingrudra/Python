a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}
result = (a & b) ^ (b & c) ^ (a & c)
print(result)
