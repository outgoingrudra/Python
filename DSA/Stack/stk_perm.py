inp=[1,2,3]
out=[2,1,3]
stk=[]
j=0
for i in inp:
    stk.append(i)
    while stk and j<len(out) and stk[-1]==out[j]:
        stk.pop();j+=1
print(j==len(out))
