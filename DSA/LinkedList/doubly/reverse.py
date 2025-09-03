class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def rev(h):
    t=None
    c=h
    while c:
        t=c.p
        c.p=c.n
        c.n=t
        c=c.p
    if t: h=t.p
    return h

h=Node(1); n2=Node(2); h.n=n2; n2.p=h
h=rev(h)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
