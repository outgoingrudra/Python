class Stack:
    def __init__(self):
        self.s = []
    def push(self,x):
        self.s.append(x)
    def pop(self):
        return self.s.pop()
st = Stack()
st.push(4)
st.push(9)
print(st.pop())
