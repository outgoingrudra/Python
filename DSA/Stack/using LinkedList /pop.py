class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def push(self,x):
        n=Node(x); n.n=self.t; self.t=n
    def pop(self):
        if not self.t: return None
        v=self.t.v; self.t=self.t.n; return v

s=Stack()
s.push(1); s.push(2)
print(s.pop())
print(s.pop())
