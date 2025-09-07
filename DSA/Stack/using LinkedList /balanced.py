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
    def isempty(self): return self.t is None

def bal(s):
    st=Stack()
    for ch in s:
        if ch in "({[":
            st.push(ch)
        else:
            t=st.pop()
            if (ch==")" and t!="(") or (ch=="]" and t!="[") or (ch=="}" and t!="{"): return False
    return st.isempty()

print(bal("([])"))
print(bal("([)]"))
