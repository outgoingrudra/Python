arr=[100,80,60,70,60,75,85]
stk=[]
span=[]
for i,p in enumerate(arr):
    while stk and arr[stk[-1]]<=p:
        stk.pop()
    span.append(i-stk[-1] if stk else i+1)
    stk.append(i)
print(span)
