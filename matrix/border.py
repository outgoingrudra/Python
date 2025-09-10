a=[[1,2,3],[4,5,6],[7,8,9]]
n=len(a)
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1: print(a[i][j],end=" ")
print()
