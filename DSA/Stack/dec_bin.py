n=13
stk=[]
while n>0:
    stk.append(str(n%2))
    n//=2
out=""
while stk:
    out+=stk.pop()
print(out)
