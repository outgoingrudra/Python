nested = [1, [2, [3, 4], 5], 6]
flat = []
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
flatten(nested)
print(flat)
