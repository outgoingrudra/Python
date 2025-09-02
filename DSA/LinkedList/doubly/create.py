class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1)
n2=Node(2)
n3=Node(3)
h.n=n2
n2.p=h
n2.n=n3
n3.p=n2

t=h
while t:
    print(t.v,end=" ")
    t=t.n
