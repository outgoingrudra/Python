expr="(a+b)*(c-d)"
stk=[]
ok=True
for c in expr:
    if c=="(":
        stk.append(c)
    elif c==")":
        if not stk: ok=False;break
        stk.pop()
print(ok and not stk)
