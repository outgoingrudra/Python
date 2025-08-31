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

    def rev_rec(self,node):
        if node is None or node.next is None:
            return node
        new=self.rev_rec(node.next)
        node.next.next=node
        node.next=None
        return new

    def reverse(self):
        self.head=self.rev_rec(self.head)

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
