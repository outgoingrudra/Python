class Queue:
    def __init__(self):
        self.q=[]
    def rev(self):
        self.q=self.q[::-1]

qq=Queue()
qq.q=[1,2,3,4]
qq.rev()
print(qq.q)
