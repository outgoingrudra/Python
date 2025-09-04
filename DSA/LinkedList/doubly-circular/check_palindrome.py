class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

a=Node(1); b=Node(2); c=Node(2); d=Node(1)
a.n=b; b.n=c; c.n=d; d.n=a
a.p=d; b.p=a; c.p=b; d.p=c
h=a

s=h; e=h.p; ok=True
while s!=e and e.n!=s:
    if s.v!=e.v: ok=False; break
    s=s.n; e=e.p
print(ok)
