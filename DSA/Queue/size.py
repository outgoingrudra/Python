class Queue:
    def __init__(self):
        self.q=[]
    def size(self):
        return len(self.q)

qq=Queue()
qq.q=[1,2,3,4]
print(qq.size())
