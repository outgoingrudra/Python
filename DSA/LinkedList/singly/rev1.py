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

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

    def show(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next

l=SLL()
for i in [1,2,3,4]:
    l.add(i)
l.reverse()
l.show()
