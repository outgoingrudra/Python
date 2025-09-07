class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def push(self,x):
        n=Node(x); n.n=self.t; self.t=n
    def size(self):
        c=0; t=self.t
        while t: c+=1; t=t.n
        return c

s=Stack()
s.push(7); s.push(8)
print(s.size())
