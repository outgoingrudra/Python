class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def push(self,x):
        n=Node(x); n.n=self.t; self.t=n
    def peek(self):
        return None if not self.t else self.t.v

s=Stack()
s.push(9); s.push(8)
print(s.peek())
