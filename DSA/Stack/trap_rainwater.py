arr=[0,1,0,2,1,0,1,3,2,1,2,1]
stk=[];res=0
for i,h in enumerate(arr):
    while stk and h>arr[stk[-1]]:
        top=stk.pop()
        if not stk: break
        dist=i-stk[-1]-1
        res+=(min(h,arr[stk[-1]])-arr[top])*dist
    stk.append(i)
print(res)
