mat=[[0,1,1],[0,0,1],[0,0,0]]
stk=list(range(len(mat)))
while len(stk)>1:
    a=stk.pop();b=stk.pop()
    if mat[a][b]==1: stk.append(b)
    else: stk.append(a)
c=stk[0]
if all(mat[c][i]==0 for i in range(len(mat))) and all(mat[i][c]==1 for i in range(len(mat)) if i!=c):
    print(c)
else: print(-1)
