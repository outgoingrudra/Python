class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def add(self,d):
        new=Node(d)
        new.next=self.head
        self.head=new

    def length(self):
        c=0
        t=self.head
        while t:
            c+=1
            t=t.next
        return c

l=SLL()
for i in [1,2,3]:
    l.add(i)
print(l.length())

