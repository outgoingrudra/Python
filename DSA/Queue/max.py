class Queue:
    def __init__(self):
        self.q=[]
    def maxi(self):
        return max(self.q) if self.q else None

qq=Queue()
qq.q=[3,8,2,10]
print(qq.maxi())
