arr=[5,10,-5]
stk=[]
for a in arr:
    while stk and a<0<stk[-1]:
        if stk[-1]<-a: stk.pop();continue
        elif stk[-1]==-a: stk.pop()
        break
    else: stk.append(a)
print(stk)
