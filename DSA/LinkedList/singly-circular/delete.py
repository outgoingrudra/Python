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
            return
        t = self.head
        while t.next != self.head:
            t = t.next
        t.next = n
        n.next = self.head

    def remove(self, val):
        if self.head is None: return
        curr = self.head
        prev = None
        while True:
            if curr.data == val:
                if prev:
                    prev.next = curr.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    self.head = curr.next
                    temp.next = self.head
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    def show(self):
        if self.head is None: return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break

l = CircleList()
for i in [10,20,30,40]:
    l.add_last(i)
l.remove(20)
l.show()
