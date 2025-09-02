class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def append(h,x):
    n=Node(x)
    if not h: return n
    t=h
    while t.n: t=t.n
    t.n=n
    n.p=t
    return h

h=None
h=append(h,5)
h=append(h,6)
h=append(h,7)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
