class Stack:
    def __init__(self):
        self.s=[]
    def top(self):
        return self.s[-1]
st=Stack()
st.s.append(10)
st.s.append(20)
print(st.top())
