class Node:
    def __init__(self,v):
        self.v=v
        self.n=None
        self.p=None

h=Node(1); h.n=Node(2); h.n.p=h
arr=[]
t=h
while t: arr.append(t.v); t=t.n
print(arr)
