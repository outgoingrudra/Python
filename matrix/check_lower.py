a=[[3,0,0],[4,5,0],[6,7,8]]
ok=all(a[i][j]==0 for i in range(3) for j in range(3) if i<j)
print(ok)
