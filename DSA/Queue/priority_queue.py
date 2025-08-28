class PQueue:
    def __init__(self):
        self.q=[]
    def push(self,val,pri):
        self.q.append((pri,val))
        self.q.sort(reverse=True)
    def pop(self):
        return self.q.pop()[1] if self.q else None

pq=PQueue()
pq.push("a",2)
pq.push("b",5)
pq.push("c",1)
print(pq.pop())
