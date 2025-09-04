class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def insaft(node,x):
    n=Node(x)
    nxt=node.n
    node.n=n; n.p=node
    n.n=nxt; nxt.p=n

a=Node(1); b=Node(2)
a.n=b; b.p=a
a.p=b; b.n=a
insaft(a,5)

t=a
while True:
    print(t.v,end=" ")
    t=t.n
    if t==a: break
