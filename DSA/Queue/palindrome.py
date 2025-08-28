class Queue:
    def __init__(self):
        self.q=[]
    def ispal(self):
        return self.q==self.q[::-1]

qq=Queue()
qq.q=[1,2,3,2,1]
print(qq.ispal())
