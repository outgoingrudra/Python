a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
res=[[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
print(res)
