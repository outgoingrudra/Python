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

    def search(self, val):
        if self.head is None: return False
        t = self.head
        while True:
            if t.data == val:
                return True
            t = t.next
            if t == self.head:
                break
        return False

l = CircleList()
for i in [7,14,21,28]:
    l.add_last(i)
print(l.search(21))
print(l.search(99))
