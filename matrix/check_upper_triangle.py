a=[[2,1,3],[0,5,6],[0,0,9]]
ok=all(a[i][j]==0 for i in range(3) for j in range(3) if i>j)
print(ok)
