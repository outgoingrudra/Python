data = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 2}
from collections import Counter
most_common_val = Counter(data.values()).most_common(1)[0][0]
print("Most common value:", most_common_val)
