arr=[6,2,5,4,5,1,6]
stk=[]
maxa=0
i=0
while i<len(arr):
    if not stk or arr[stk[-1]]<=arr[i]:
        stk.append(i);i+=1
    else:
        top=stk.pop()
        area=arr[top]*((i-stk[-1]-1) if stk else i)
        maxa=max(maxa,area)
while stk:
    top=stk.pop()
    area=arr[top]*((i-stk[-1]-1) if stk else i)
    maxa=max(maxa,area)
print(maxa)
