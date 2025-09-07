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
        v=self.t.v; self.t=self.t.n; return v
    def isempty(self): return self.t is None
    def sort(self):
        tmp=Stack()
        while not self.isempty():
            x=self.pop()
            while not tmp.isempty() and tmp.t.v<x:
                self.push(tmp.pop())
            tmp.push(x)
        self.t=tmp.t
    def show(self):
        t=self.t
        while t: print(t.v,end=" "); t=t.n

s=Stack()
s.push(3); s.push(1); s.push(2)
s.sort()
s.show()
