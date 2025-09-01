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

    def remove_head(self):
        if self.head is None: return
        if self.head.next == self.head:
            self.head = None
            return
        t = self.head
        while t.next != self.head:
            t = t.next
        self.head = self.head.next
        t.next = self.head

    def show(self):
        if self.head is None: return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break

l = CircleList()
for i in [1,2,3,4]:
    l.add_last(i)
l.remove_head()
l.show()
