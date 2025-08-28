from collections import deque
q=deque([1,2,3,4,5,6])
half=len(q)//2
q1=list(q)[:half]
q2=list(q)[half:]
ans=[]
for i in range(half):
    ans.append(q1[i])
    ans.append(q2[i])
print(ans)
