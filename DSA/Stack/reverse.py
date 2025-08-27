txt="hello"
stk=[]
for c in txt:
    stk.append(c)
out=""
while stk:
    out+=stk.pop()
print(out)
