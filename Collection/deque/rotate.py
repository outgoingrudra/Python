from collections import deque

dq = deque([10, 20, 30, 40, 50])
dq.rotate(2)
print(dq)

dq.rotate(-1)
print(dq)
