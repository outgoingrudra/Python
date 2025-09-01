class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class CircleList:
    def __init__(self):
        self.head = None

    def add_last(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
            new.next = new
        else:
            t = self.head
            while t.next != self.head:
                t = t.next
            t.next = new
            new.next = self.head

    def show(self):
        if self.head is None: return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break

l = CircleList()
l.add_last(5)
l.add_last(15)
l.add_last(25)
l.show()
