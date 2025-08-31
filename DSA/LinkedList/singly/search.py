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

    def search(self,x):
        t=self.head
        while t:
            if t.data==x: return True
            t=t.next
        return False

l=SLL()
l.add(5)
l.add(10)
print(l.search(10))
print(l.search(7))
