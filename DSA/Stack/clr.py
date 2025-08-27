class Stack:
    def __init__(self):
        self.s=[]
    def clear(self):
        self.s=[]
st=Stack()
st.s.extend([5,6,7])
st.clear()
print(st.s)
