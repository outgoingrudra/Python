class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, v):
        n = Node(v)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def mid(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.v

l = LinkedList()
for i in [10,20,30,40,50]:
    l.add(i)
print("Middle:", l.mid())
