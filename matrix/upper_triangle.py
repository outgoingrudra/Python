a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if j<i: print(" ",end=" ")
        else: print(a[i][j],end=" ")
    print()
