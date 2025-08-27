stk=[34,3,31,98,92,23]
tmp=[]
while stk:
    t=stk.pop()
    while tmp and tmp[-1]>t:
        stk.append(tmp.pop())
    tmp.append(t)
print(tmp)
