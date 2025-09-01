class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def add(self,d):
        new=Node(d)
        if not self.head:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new

    def remove_dup(self):
        t=self.head
        while t and t.next:
            if t.data==t.next.data:
                t.next=t.next.next
            else:
                t=t.next

    def show(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next

l=SLL()
for i in [1,1,2,3,3]:
    l.add(i)
l.remove_dup()
l.show()
