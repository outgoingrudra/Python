a=[[9,8],[7,6]]
b=[[5,4],[3,2]]
res=[[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
print(res)
