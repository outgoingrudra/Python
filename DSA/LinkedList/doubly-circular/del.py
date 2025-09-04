class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def delval(h,x):
    if not h: return None
    t=h
    while True:
        if t.v==x:
            if t.n==t: return None
            t.p.n=t.n
            t.n.p=t.p
            if t==h: h=t.n
            break
        t=t.n
        if t==h: break
    return h

a=Node(1); b=Node(2); c=Node(3)
a.n=b; b.n=c; c.n=a
a.p=c; b.p=a; c.p=b
h=a
h=delval(h,2)

t=h
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h: break
