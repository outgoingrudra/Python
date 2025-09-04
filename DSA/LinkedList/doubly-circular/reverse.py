class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

a=Node(1); b=Node(2); c=Node(3)
a.n=b; b.n=c; c.n=a
a.p=c; b.p=a; c.p=b

t=a.p
while True:
    print(t.v,end=" ")
    t=t.p
    if t==a.p: break
