class MinStack:
    def __init__(self):
        self.s=[];self.m=[]
    def push(self,x):
        self.s.append(x)
        self.m.append(x if not self.m else min(x,self.m[-1]))
    def pop(self):
        self.m.pop();return self.s.pop()
    def getmin(self): return self.m[-1]
st=MinStack()
st.push(3);st.push(5);st.push(2)
print(st.getmin())
