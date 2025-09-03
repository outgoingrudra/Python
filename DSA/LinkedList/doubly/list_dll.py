class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

a=[1,2,3]
h=Node(a[0]); t=h
for i in a[1:]:
    n=Node(i)
    t.n=n
    n.p=t
    t=n

x=h
while x: print(x.v,end=" "); x=x.n
