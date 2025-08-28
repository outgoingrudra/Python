class CQueue:
    def __init__(self,n):
        self.q=[None]*n
        self.size=n
        self.front=self.rear=-1
    def enqueue(self,val):
        if (self.rear+1)%self.size==self.front: return "full"
        if self.front==-1: self.front=0
        self.rear=(self.rear+1)%self.size
        self.q[self.rear]=val
    def dequeue(self):
        if self.front==-1: return None
        x=self.q[self.front]
        if self.front==self.rear: self.front=self.rear=-1
        else: self.front=(self.front+1)%self.size
        return x

cq=CQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.dequeue())
