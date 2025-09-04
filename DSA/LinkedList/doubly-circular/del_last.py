class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def delend(h):
    if not h or h.n==h: return None
    l=h.p
    l.p.n=h
    h.p=l.p
    return h

a=Node(1); b=Node(2); c=Node(3)
a.n=b; b.n=c; c.n=a
a.p=c; b.p=a; c.p=b
h=a
h=delend(h)

t=h
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h: break
