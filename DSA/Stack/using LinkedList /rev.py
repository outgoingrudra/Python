class Node:
    def __init__(self,v):
        self.v=v
        self.n=None

class Stack:
    def __init__(self):
        self.t=None
    def push(self,x):
        n=Node(x); n.n=self.t; self.t=n
    def rev(self):
        prev=None; cur=self.t
        while cur:
            nxt=cur.n
            cur.n=prev
            prev=cur
            cur=nxt
        self.t=prev
    def show(self):
        t=self.t
        while t: print(t.v,end=" "); t=t.n

s=Stack()
s.push(1); s.push(2); s.push(3)
s.rev()
s.show()
