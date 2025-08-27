arr=[4,5,2,25]
stk=[]
ans=[]
for x in arr[::-1]:
    while stk and stk[-1]<=x:
        stk.pop()
    ans.append(stk[-1] if stk else -1)
    stk.append(x)
print(ans[::-1])
