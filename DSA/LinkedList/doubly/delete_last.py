class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def del_end(h):
    if not h or not h.n: return None
    t=h
    while t.n: t=t.n
    t.p.n=None
    return h

h=Node(1); h.n=Node(2); h.n.p=h
h=del_end(h)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
