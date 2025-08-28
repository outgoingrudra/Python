class Queue:
    def __init__(self):
        self.q=[]
    def sumq(self):
        return sum(self.q)

qq=Queue()
qq.q=[4,5,6]
print(qq.sumq())
