class Queue:
    def __init__(self):
        self.q=[]
    def median(self):
        s=sorted(self.q)
        n=len(s)
        if n%2: return s[n//2]
        return (s[n//2-1]+s[n//2])/2

qq=Queue()
qq.q=[7,1,5,3]
print(qq.median())
