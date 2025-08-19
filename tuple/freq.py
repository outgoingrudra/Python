tuples = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
freq = {}
for t in tuples:
    freq[t] = freq.get(t, 0) + 1
print(freq)
