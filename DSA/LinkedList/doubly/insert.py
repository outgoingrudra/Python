class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

def push(h,x):
    n=Node(x)
    n.n=h
    if h: h.p=n
    return n

h=None
h=push(h,10)
h=push(h,20)
t=h
while t:
    print(t.v,end=" ")
    t=t.n
