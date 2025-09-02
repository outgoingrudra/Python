class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1); n2=Node(2); h.n=n2; n2.p=h
t=n2
while t:
    print(t.v,end=" ")
    t=t.p
