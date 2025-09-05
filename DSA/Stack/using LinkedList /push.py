class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def push(self,x):
        n=Node(x)
        n.n=self.t
        self.t=n

s=Stack()
s.push(5)
s.push(10)
print(s.t.v)
