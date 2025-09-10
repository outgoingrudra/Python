a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    a[i][0],a[i][-1]=a[i][-1],a[i][0]
print(a)
