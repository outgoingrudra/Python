a=[[1,2],[3,4]]
b=[[2,0],[1,2]]
res=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            res[i][j]+=a[i][k]*b[k][j]
print(res)
