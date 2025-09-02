class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def insert_after(node,x):
    if not node: return
    n=Node(x)
    n.n=node.n
    node.n=n
    n.p=node
    if n.n: n.n.p=n

h=Node(1)
h.n=Node(2); h.n.p=h
insert_after(h,9)

t=h
while t:
    print(t.v,end=" ")
    t=t.n
