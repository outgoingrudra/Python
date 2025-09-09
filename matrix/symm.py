a=[[1,2,3],[2,5,6],[3,6,9]]
ok=all(a[i][j]==a[j][i] for i in range(3) for j in range(3))
print(ok)
