a=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
top,down,left,right=0,2,0,2
while top<=down and left<=right:
    for i in range(left,right+1): res.append(a[top][i])
    top+=1
    for i in range(top,down+1): res.append(a[i][right])
    right-=1
    if top<=down:
        for i in range(right,left-1,-1): res.append(a[down][i])
        down-=1
    if left<=right:
        for i in range(down,top-1,-1): res.append(a[i][left])
        left+=1
print(res)
