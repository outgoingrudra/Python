s="abbaca"
stk=[]
for c in s:
    if stk and stk[-1]==c: stk.pop()
    else: stk.append(c)
print("".join(stk))
