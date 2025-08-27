expr="((a+b))"
stk=[]
dup=False
for c in expr:
    if c==")":
        cnt=0
        while stk and stk[-1]!="(":
            stk.pop();cnt+=1
        stk.pop()
        if cnt<=1: dup=True;break
    else:
        stk.append(c)
print(dup)
