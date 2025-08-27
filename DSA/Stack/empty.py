class Stack:
    def __init__(self):
        self.s=[]
    def empty(self):
        return len(self.s)==0
st=Stack()
print(st.empty())
st.s.append(1)
print(st.empty())
