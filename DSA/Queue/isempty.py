class Queue:
    def __init__(self):
        self.q = []
    def empty(self):
        return len(self.q)==0

qq = Queue()
print(qq.empty())
qq.q.append(1)
print(qq.empty())
