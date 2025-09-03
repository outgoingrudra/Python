class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1); n2=Node(1); n3=Node(2)
h.n=n2; n2.p=h; n2.n=n3; n3.p=n2

seen=set(); t=h
while t:
    if t.v in seen:
        if t.p: t.p.n=t.n
        if t.n: t.n.p=t.p
    else: seen.add(t.v)
    t=t.n

x=h
while x: print(x.v,end=" "); x=x.n
