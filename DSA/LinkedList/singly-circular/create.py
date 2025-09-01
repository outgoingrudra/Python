class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class CircleList:
    def __init__(self):
        self.head = None

    def add_front(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
            new.next = new
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            new.next = self.head
            self.head = new

    def show(self):
        if self.head is None: return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break

l = CircleList()
l.add_front(10)
l.add_front(20)
l.add_front(30)
l.show()
