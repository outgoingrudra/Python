class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1); h.n=Node(2); h.n.p=h
c=0; t=h
while t: c+=1; t=t.n
print(c)
