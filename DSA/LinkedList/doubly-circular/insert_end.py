class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def insend(h,x):
    n=Node(x)
    if not h:
        n.n=n; n.p=n
        return n
    l=h.p
    n.n=h; h.p=n
    n.p=l; l.n=n
    return h

h=None
h=insend(h,1)
h=insend(h,2)
h=insend(h,3)

t=h
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h: break
