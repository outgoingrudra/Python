class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, val):
        self.q.append(val)
    def dequeue(self):
        if not self.q: return None
        return self.q.pop(0)
    def show(self):
        return self.q

qq = Queue()
qq.enqueue(5)
qq.enqueue(7)
print(qq.show())
print(qq.dequeue())
print(qq.show())
