expr="a+b*c"
stk=[]
out=""
prec={'+':1,'-':1,'*':2,'/':2}
for c in expr:
    if c.isalnum():
        out+=c
    else:
        while stk and prec.get(stk[-1],0)>=prec.get(c,0):
            out+=stk.pop()
        stk.append(c)
while stk: out+=stk.pop()
print(out)
