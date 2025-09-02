class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def del_front(h):
    if not h: return None
    h=h.n
    if h: h.p=None
    return h

h=Node(1); h.n=Node(2); h.n.p=h
h=del_front(h)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
