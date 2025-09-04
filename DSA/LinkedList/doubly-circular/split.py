class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def split(h):
    if not h or h.n==h: return h,None
    s=f=h
    while f.n!=h and f.n.n!=h:
        f=f.n.n
        s=s.n
    h2=s.n
    s.n=h; h.p=s
    f=f.n if f.n!=h else f
    f.n=h2; h2.p=f
    return h,h2

a=Node(1); b=Node(2); c=Node(3); d=Node(4)
a.n=b; b.n=c; c.n=d; d.n=a
a.p=d; b.p=a; c.p=b; d.p=c
h1,h2=split(a)

t=h1
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h1: break
print("|",end=" ")
t=h2
while True:
    print(t.v,end=" ")
    t=t.n
    if t==h2: break
