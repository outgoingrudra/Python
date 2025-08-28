from collections import deque
names=["a","b","c","d","e"]
q=deque(names)
while len(q)>1:
    q.rotate(-3)
    q.pop()
print(q[0])
