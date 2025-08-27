expr="+9*26"
stk=[]
for c in expr[::-1]:
    if c.isdigit():
        stk.append(int(c))
    else:
        a=stk.pop();b=stk.pop()
        if c=="+": stk.append(a+b)
        elif c=="-": stk.append(a-b)
        elif c=="*": stk.append(a*b)
print(stk[0])
