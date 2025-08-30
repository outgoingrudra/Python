class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, x):
        n = Node(x)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def remove(self, key):
        if self.head and self.head.val == key:
            self.head = self.head.next
            return
        t = self.head
        while t and t.next:
            if t.next.val == key:
                t.next = t.next.next
                return
            t = t.next

    def show(self):
        t = self.head
        while t:
            print(t.val, end=" ")
            t = t.next

l = LinkedList()
for i in [1,2,3,4,5]:
    l.add(i)
l.remove(3)
l.show()
