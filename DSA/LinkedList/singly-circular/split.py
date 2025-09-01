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

    def split(self):
        if self.head is None: return None, None
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        head1 = self.head
        head2 = slow.next
        slow.next = head1
        t = head2
        while t.next != self.head:
            t = t.next
        t.next = head2
        return head1, head2

    def show(self, h):
        if h is None: return
        t = h
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == h:
                break
        print()

l = CircleList()
for i in [1,2,3,4,5,6]:
    l.add_last(i)
h1, h2 = l.split()
l.show(h1)
l.show(h2)
