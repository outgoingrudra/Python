a=[[0,2,-1],[-2,0,-4],[1,4,0]]
ok=all(a[i][j]==-a[j][i] for i in range(3) for j in range(3))
print(ok)
