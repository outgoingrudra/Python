from collections import deque
jobs=[("A",2),("B",1),("C",3)]
q=deque(jobs)
time=0
while q:
    j,t=q.popleft()
    time+=t
    print(j,"done at",time)
