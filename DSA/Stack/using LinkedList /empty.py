class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def isempty(self):
        return self.t is None

s=Stack()
print(s.isempty())
