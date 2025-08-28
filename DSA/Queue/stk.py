from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft() if self.q else None

s=MyStack()
s.push(1)
s.push(2)
print(s.pop())
