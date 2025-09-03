class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1); h.n=Node(2); h.n.p=h
x=2
t=h; f=False
while t:
    if t.v==x: f=True; break
    t=t.n
print(f)
