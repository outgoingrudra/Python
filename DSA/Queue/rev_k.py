from collections import deque
def revk(q,k):
    arr=[]
    for i in range(k):
        arr.append(q.popleft())
    arr.reverse()
    q=deque(arr)+q
    return q

q=deque([1,2,3,4,5,6])
print(revk(q,3))
