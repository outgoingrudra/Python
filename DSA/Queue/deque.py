from collections import deque
d=deque()
d.append(1)
d.appendleft(2)
d.append(3)
print(d)
d.pop()
d.popleft()
print(d)
