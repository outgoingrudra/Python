class Stack:
    def __init__(self):
        self.s=[]
    def size(self):
        return len(self.s)
st=Stack()
st.s.extend([1,2,3])
print(st.size())
