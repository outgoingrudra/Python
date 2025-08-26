from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)

dq.pop()
dq.popleft()
print(dq)
