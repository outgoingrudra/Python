class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def show(self):
        t = self.head
        while t:
            print(t.v, end=" ")
            t = t.next

l = LinkedList()
for i in [1,2,3,4]:
    l.push(i)
l.reverse()
l.show()
