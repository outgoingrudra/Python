class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

a=Node(1); b=Node(2); c=Node(3)
a.n=b; b.p=a; b.n=c; c.p=b; c.n=a; a.p=c

t=a
while True:
    print(t.v,end=" ")
    t=t.n
    if t==a: break
