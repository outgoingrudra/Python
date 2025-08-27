expr="23*54*+"
stk=[]
for c in expr:
    if c.isdigit():
        stk.append(int(c))
    else:
        b=stk.pop();a=stk.pop()
        if c=="+": stk.append(a+b)
        elif c=="-": stk.append(a-b)
        elif c=="*": stk.append(a*b)
        elif c=="/": stk.append(a//b)
print(stk[0])
