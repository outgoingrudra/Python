edges = [("A", "B"), ("A", "C"), ("B", "D")]
graph = {}
for a, b in edges:
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
print(graph)
