class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def del_node(h,val):
    t=h
    while t and t.v!=val: t=t.n
    if not t: return h
    if t.p: t.p.n=t.n
    else: h=t.n
    if t.n: t.n.p=t.p
    return h

h=Node(1); h.n=Node(2); h.n.p=h
h=del_node(h,2)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
