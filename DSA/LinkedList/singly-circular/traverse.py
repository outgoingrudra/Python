class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class CircleList:
    def __init__(self):
        self.head = None

    def add_last(self, v):
        n = Node(v)
        if self.head is None:
            self.head = n
            n.next = n
        else:
            t = self.head
            while t.next != self.head:
                t = t.next
            t.next = n
            n.next = self.head

    def traverse(self):
        if self.head is None: return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break

l = CircleList()
for i in [11,22,33,44]:
    l.add_last(i)
l.traverse()
