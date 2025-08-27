class TwoStacks:
    def __init__(self,n):
        self.arr=[0]*n;self.top1=-1;self.top2=n
    def push1(self,x):
        self.top1+=1;self.arr[self.top1]=x
    def push2(self,x):
        self.top2-=1;self.arr[self.top2]=x
ts=TwoStacks(10)
ts.push1(5);ts.push2(9)
print(ts.arr)
