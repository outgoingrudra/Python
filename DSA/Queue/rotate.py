class Queue:
    def __init__(self):
        self.q=[]
    def rotate(self,k):
        k=k%len(self.q)
        self.q=self.q[k:]+self.q[:k]

qq=Queue()
qq.q=[1,2,3,4,5]
qq.rotate(2)
print(qq.q)
