class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def insbeg(h,x):
    n=Node(x)
    if not h:
        n.n=n; n.p=n
        return n
    l=h.p
    n.n=h; n.p=l
    h.p=n; l.n=n
    return n

h=None
h=insbeg(h,1)
h=insbeg(h,2)
h=insbeg(h,3)

t=h
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h: break
