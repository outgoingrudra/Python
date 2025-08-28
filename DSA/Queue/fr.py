class Queue:
    def __init__(self):
        self.q = []
    def front(self):
        return self.q[0] if self.q else None
    def rear(self):
        return self.q[-1] if self.q else None

qq = Queue()
qq.q = [10,20,30]
print(qq.front(), qq.rear())
