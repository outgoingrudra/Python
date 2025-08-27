class MaxStack:
    def __init__(self):
        self.s=[];self.mx=[]
    def push(self,x):
        self.s.append(x)
        self.mx.append(x if not self.mx else max(x,self.mx[-1]))
    def pop(self):
        self.mx.pop();return self.s.pop()
    def getmax(self): return self.mx[-1]
st=MaxStack()
st.push(1);st.push(9);st.push(3)
print(st.getmax())
