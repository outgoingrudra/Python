a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    if i%2==0: print(*a[i])
    else: print(*a[i][::-1])
