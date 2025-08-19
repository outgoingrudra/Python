tuples = [(1, 2), (3, 4), (0, 9)]
max_t = max(tuples, key=sum)
min_t = min(tuples, key=sum)
print("Max:", max_t, "Min:", min_t)
