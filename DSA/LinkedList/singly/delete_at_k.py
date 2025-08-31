class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class SLL:
    def __init__(self):
        self.head=None

    def insert(self,d):
        new=Node(d)
        if not self.head:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new

    def del_pos(self,pos):
        if self.head is None: return
        if pos==0:
            self.head=self.head.next
            return
        t=self.head
        for _ in range(pos-1):
            if t is None: return
            t=t.next
        if t and t.next:
            t.next=t.next.next

    def show(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next

l=SLL()
for i in [1,2,3,4]:
    l.insert(i)
l.del_pos(2)
l.show()
