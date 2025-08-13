data = {"x": [1, 2], "y": [3, 4], "z": [5]}
flat = [item for sublist in data.values() for item in sublist]
print(flat)
